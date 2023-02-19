from app import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from datetime import datetime




class BlogEntry(db.Model, SerializerMixin):
    __tablename__ = "blog_entries"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    message = db.Column(db.String(280))
    email = db.Column(db.String(50))
    date_created = db.Column(DateTime(timezone=True), server_default=func.now())
    date_updated = db.Column(DateTime, default=datetime.utcnow, onupdate=func.now())


    
    
    def __init__(self, name,message,email):
        self.name = name
        self.message = message
        self.email = email

        # self.date_created = datetime.datetime.now()
        # self.date_updated = datetime.datetime.now()

    def update(self, name,message,email):
        self.name = name
        self.message = message
        self.email = email
        # self.date_updated = datetime.datetime.now()