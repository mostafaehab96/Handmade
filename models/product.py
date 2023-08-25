"""
Contains Product class
"""
from models.base_model import BaseModel
from models import db

class Product(BaseModel, db.Model):
    __tablename__ = "products"
    name = db.Column(db.String(60))
    description = db.Column(db.String(1024))
    image = db.Column(db.String(512), nullable=False)
    price = db.Column(db.Float)
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)
    reviews= db.relationship("Review")