"""Blueprint for flask routes"""

from flask import Blueprint
app_views = Blueprint("app_views", __name__)

from web_flask.views.products import *
from web_flask.views.cart import *
from web_flask.views.account import *
from web_flask.views.orders import *
from web_flask.views.login import *