"""
Contains Review class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer

class Review(BaseModel, Base):
    __tablename__ = "reviews"
    text = Column(String(1024))
    user_id = Column(String(60), ForeignKey("users.id"))
    product_id = Column(String(60), ForeignKey("products.id"))
    rating = Column(Integer, nullable=True)