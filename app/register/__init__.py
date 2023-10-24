from flask import Blueprint
from flask_bootstrap import Bootstrap

bp = Blueprint('register', __name__)

from app.register import routes
