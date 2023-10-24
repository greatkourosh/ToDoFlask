from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user
from app.register import bp
from app.extensions import db
from flask_bootstrap import Bootstrap

from app.models.user import User
from forms import RegisterForm


# from app.models.post import Post
@bp.route('/', methods=['GET', 'POST'])
def index():
    register_form = RegisterForm()
    if request.method == 'POST':
        if register_form.validate_on_submit():
            # If user's email already exists
            if User.query.filter_by(email=register_form.email.data).first():
                # Send flash messsage
                flash("You've already signed up with that email, log in instead!")
                # Redirect to /login route.
                return redirect(url_for('login'))
            hash_and_salted_password = generate_password_hash(
                register_form.password.data,
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = User(
                email=register_form.email.data,
                name=register_form.name.data,
                password=hash_and_salted_password,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("main.index"))
    # posts = Post.query.all()
    return render_template('register/index.html', form=register_form, logged_in=current_user.is_authenticated, user=current_user)

# @bp.route('/categories/')
# def categories():
#     return render_template('posts/categories.html')