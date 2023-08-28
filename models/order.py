"""
Contains Order class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship

orders_products = Table(
    "orders_products",
    Base.metadata,
    Column("order_id", String(60), ForeignKey("orders.id"), primary_key=True),
    Column("product_id", String(60), ForeignKey("products.id"), primary_key=True)
    )


class Order(BaseModel, Base):
    __tablename__ = "orders"
    address = Column(String(256))
    total_price = Column(Float)
    user_id = Column(String(60), ForeignKey("users.id"))
    products = relationship("Product", secondary=orders_products)
