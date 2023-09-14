"""
Handles operations regarding the database storage
"""
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.product import Product
from models.order import Order
from models.review import Review
from models.category import Category
from models.cart import Cart


class DBStorage:
    __engine = None
    __session = None
    __classes = {"User": User, "Product": Product, "Order": Order,
                 "Review": Review, "Category": Category, "Cart": Cart
                 }

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://handmade_dev:0000@localhost/handmade_db"
        )

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def drop(self):
        """Drops all data"""
        Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """Adds new instance to the session scope"""
        if obj is not None:
            self.__session.add(obj)

    def delete(self, obj):
        """Deletes the instance from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        """Commits changes to database"""
        self.__session.commit()

    def close(self):
        """Removes the session from the registry of scoped sessions"""
        self.__session.remove()

    def all(self, cls=None):
        """Gets all records for a specific table or
        for all tables"""
        if cls is None:
            all_dict = {}
            for clas in self.__classes:
                records = self.__session.query(clas).all()
                all_dict[clas.__name__] = records
            return all_dict
        clas = self.__classes.get(cls, None)
        if clas is not None:
            return self.__session.query(clas).all()

        return None

    def get(self, cls, id):
        """Returns an object based on class name and id"""
        if cls not in self.__classes.keys():
            return None

        clas = self.__classes.get(cls)
        return self.__session.query(clas).filter_by(id=id).first()

    def filter(self, cls, col, value):
        """Returns an abject based on the class name, column and value to filter"""
        if cls not in self.__classes.keys():
            return None

        clas = self.__classes.get(cls)
        attr = getattr(clas, col, None)
        if attr:
            return self.__session.query(clas).filter(attr == value).first()
        else:
            return None
