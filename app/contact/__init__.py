from flask import Blueprint
from flask_bootstrap import Bootstrap

bp = Blueprint('contact', __name__)

from app.contact import routes
