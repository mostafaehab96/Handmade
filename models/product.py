"""
Contains Product class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship


product_categories = Table(
    "products_categories",
    Base.metadata,
    Column("product_id", String(60), ForeignKey("products.id"), primary_key=True),
    Column("category_id", String(60), ForeignKey("categories.id"), primary_key=True)
)


class Product(BaseModel, Base):
    __tablename__ = "products"
    name = Column(String(60))
    description = Column(String(1024))
    image = Column(String(512), nullable=False)
    price = Column(Float)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    reviews = relationship("Review")
    categories = relationship("Category", secondary=product_categories,
                                 backref="products")
