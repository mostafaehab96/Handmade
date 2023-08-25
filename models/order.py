"""
Contains Order class
"""
from models.base_model import BaseModel
from models import db

orders_products = db.Table(
    "orders_products",
    db.Column("order_id", db.String(60), db.ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", db.String(60), db.ForeignKey("products.id"), primary_key=True)
    )


class Order(BaseModel, db.Model):
    __tablename__ = "orders"
    address = db.Column(db.String(256))
    total_price = db.Column(db.Float)
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"))
    products = db.relationship("Product", secondary=orders_products)
