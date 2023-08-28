"""Blueprint for the API"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api')

from api.views.index import *
from api.views.users import *
from api.views.products import *
from api.views.orders import *
from api.views.categories import *
from api.views.reviews import *
