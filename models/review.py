"""
Contains Review class
"""

from models.base_model import BaseModel
from models import db

class Review(BaseModel, db.Model):
    __tablename__ = "reviews"
    text = db.Column(db.String(1024))
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"))
    product_id = db.Column(db.String(60), db.ForeignKey("products.id"))