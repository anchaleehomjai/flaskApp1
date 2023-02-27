from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from app import db
from .blogentry import BlogEntry

class AuthUser_lab13(db.Model, UserMixin):
    __tablename__ = "auth_users_lab13"
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    avatar_url = db.Column(db.String(100))

    def __init__(self, email, name, password, avatar_url):
        self.email = email
        self.name = name
        self.password = password
        self.avatar_url = avatar_url

class PrivateContact_lab13(BlogEntry, UserMixin, SerializerMixin):
    owner_id = db.Column(db.Integer, db.ForeignKey('auth_users_lab13.id'))

    def __init__(self, name,message,email,owner_id,avatar_url):
        super().__init__(name,message,email,avatar_url)
        self.owner_id = owner_id
