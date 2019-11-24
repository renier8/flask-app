from flask import Flask
from flaskr.db import db_session, Base
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskr.config import Config
from flask_uploads import UploadSet, IMAGES, configure_uploads

photos = UploadSet('photos', IMAGES)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)
    migrate = Migrate(app, Base)

    configure_uploads(app, photos)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    from . import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    

    return app