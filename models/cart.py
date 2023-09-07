from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship



products_carts = Table(
    "products_carts",
    Base.metadata,
    Column("cart_id", String(60), ForeignKey("carts.id"), primary_key=True),
    Column("product_id", String(60), ForeignKey("products.id"), primary_key=True)
)
class Cart(BaseModel, Base):
    __tablename__ = "carts"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    products = relationship("Product", secondary=products_carts)
