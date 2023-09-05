"""
Contains User class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class User(BaseModel, Base, UserMixin):
    __tablename__ = "users"
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128), nullable=False)
    address = Column(String(128))
    postal_code = Column(String(10))
    about = Column(String(1024))
    products = relationship("Product", backref="user", cascade="all, delete")
    orders = relationship("Order", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = generate_password_hash(value, salt_length=8, method='pbkdf2:sha256')
        super().__setattr__(name, value)


