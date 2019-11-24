from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.db import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(String(50))
    gender = Column(String(10))
    relationship_status = Column(String(50))
    current_city = Column(String(50))
    bio = Column(String(150))
    profile_pic = Column(String(50))
    day = Column(String(5))
    month = Column(String(12))
    year = Column(String(7))
    posts = relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    body = Column(String(140), nullable=False)
    created = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '<Body %r>' % (self.body)
