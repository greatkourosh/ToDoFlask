from flask import render_template
from app.main import bp
from flask_login import current_user

@bp.route('/')
def index():
    return render_template('index.html', logged_in=current_user.is_authenticated, user=current_user)
