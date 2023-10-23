from flask import Blueprint
from flask_bootstrap import Bootstrap

bp = Blueprint('login', __name__)

from app.login import routes
