"""
Handles operations regarding the database storage
"""


class DBStorage:
    __session = None

    def __init__(self, db):
        self.__session = db.session

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
