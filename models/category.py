from models import db
from models.base_model import BaseModel




class Category(BaseModel, db.Model):
    __tablename__ = "categories"
    name = db.Column(db.String(60))
