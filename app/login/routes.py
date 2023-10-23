from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user
from app.login import bp
from app.extensions import db
from flask_bootstrap import Bootstrap

from app.models.user import User
from forms import LoginForm


# from app.models.post import Post
@bp.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            email = login_form.email.data
            password = login_form.password.data
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    flash('You were successfully logged in')
                    print("You successfully logged in")
                    # return redirect(url_for('get_all_posts', user_id=user.id))
                    return redirect(url_for('main.index', user_id=user.id))
                else:
                    flash('Your password seems wrong, try again!')
                    print("Sorry, Access Denied!")
                    return redirect(url_for('login.index'))
            else:
                # error = 'Invalid credentials'
                flash('The Email doesnt Exist. Please try again!')
                print("Sorry, Access Denied!")
                return redirect(url_for('login.index'))
    # posts = Post.query.all()
    return render_template('login/index.html', form=login_form, logged_in=current_user.is_authenticated, user=current_user)

# @bp.route('/categories/')
# def categories():
#     return render_template('posts/categories.html')