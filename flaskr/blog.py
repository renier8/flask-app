from flask import Blueprint, render_template, redirect, url_for, request, g
from flaskr.auth import login_required
from flaskr.models import Post, User
from flaskr.db import db_session
from werkzeug.exceptions import abort
from flaskr import photos

bp = Blueprint('blog', __name__)

from flaskr import photos
@bp.route('/')
def index():
    posts = Post.query.order_by(Post.created.desc()).all()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        body = request.form['body']

        post = Post(body=body, author=g.user)
        db_session.add(post)
        db_session.commit()
        return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = Post.query.filter(Post.id == id).first()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post.user_id != g.user.id:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        body = request.form['body']

        post.body = body
        db_session.add(post)
        db_session.commit()
        return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = get_post(id)
    db_session.delete(post)
    db_session.commit()
    return redirect(url_for('blog.index'))

@bp.route('/<username>')
def profile(username):
    user = User.query.filter(User.username == username).first()
    posts = Post.query.filter(Post.user_id == user.id).order_by(Post.created.desc())
    return render_template('blog/profile.html', user=user, posts=posts)

@bp.route('/<username>/edit_profile', methods=('POST', 'GET'))
@login_required
def edit_profile(username):
    user = User.query.filter(User.username == username).first()
    posts = Post.query.filter(Post.user_id == user.id).order_by(Post.created.desc())
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')
        gender = request.form['gender']
        relationship_status = request.form['relationship_status']
        current_city = request.form['current_city']
        bio = request.form['bio']
        user.first_name = first_name
        user.last_name = last_name
        user.date_of_birth = ''
        user.day = day
        user.month = month
        user.year = year
        user.gender = gender
        user.relationship_status = relationship_status
        user.current_city = current_city
        user.bio = bio
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                user.profile_pic = photos.save(request.files['photo'])
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('blog.profile', username=user.username))
    return render_template('blog/edit_profile.html', user=user)