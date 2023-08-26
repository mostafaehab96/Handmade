"""
Contains Product class
"""
from models.base_model import BaseModel
from models import db
from models.category import Category

product_categories  = db.Table(
    "products_categories",
    db.Column("product_id", db.String(60), db.ForeignKey("products.id"), primary_key=True),
    db.Column("category_id", db.String(60), db.ForeignKey("categories.id"), primary_key=True)
    )

class Product(BaseModel, db.Model):
    __tablename__ = "products"
    name = db.Column(db.String(60))
    description = db.Column(db.String(1024))
    image = db.Column(db.String(512), nullable=False)
    price = db.Column(db.Float)
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)
    reviews= db.relationship("Review")
    categories = db.relationship("Category", secondary=product_categories)