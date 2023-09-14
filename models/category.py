from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Category(BaseModel, Base):
    __tablename__ = "categories"
    name = Column(String(60))
