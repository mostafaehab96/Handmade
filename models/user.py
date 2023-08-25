"""
Contains User class
"""
from models.base_model import BaseModel
from models import db


class User(BaseModel, db.Model):
    __tablename__ = "users"
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(60))
    address = db.Column(db.String(128))
    postal_code = db.Column(db.String(10))
    about = db.Column(db.String(1024))
    products = db.relationship("Product", backref="user", cascade="all, delete")
    orders = db.relationship("Order", backref="user", cascade="all, delete")
    reviews = db.relationship("Review", backref="user", cascade="all, delete")

