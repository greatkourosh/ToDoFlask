from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from app import create_app
# from flask_login import UserMixin, login_user, login_required, current_user, logout_user, LoginManager
# from flask_gravatar import Gravatar
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# ckeditor = CKEditor(app)
# Bootstrap(app)


# @app.route("/", methods=['GET'])
# def home():
#     return render_template("index.html")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    create_app().run(host='127.0.0.1', port=5000, debug=True)
