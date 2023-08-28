from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models.engine.db_storage import DBStorage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://handmade_dev:0000@localhost/handmade_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

storage = DBStorage(db=db)
