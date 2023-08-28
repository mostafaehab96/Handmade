"""
Defines the base model for all classes
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
import models
from datetime import datetime
import uuid

Base = declarative_base()


class BaseModel:
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def to_dict(self):
        """Returns dictionary representation of the class"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        if "password" in new_dict:
            del new_dict["password"]
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        return new_dict

    def save(self):
        """Saving current instance"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete current instance"""
        models.storage.delete(self)

