from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user
from app.contact import bp
from app.extensions import db
from flask_bootstrap import Bootstrap

from app.models.user import User
from forms import ContactForm


# from app.models.post import Post
@bp.route('/', methods=['GET', 'POST'])
def index():
    contact_form = ContactForm()
    if request.method == 'POST':
        if contact_form.validate_on_submit():
            # If user's email already exists
            name = contact_form.name.data
            email = contact_form.email.data
            phone_number = contact_form.phone.data
            message = contact_form.message.data

            # db.session.add(new_user)
            # db.session.commit()
            # login_user(new_user)
            return redirect(url_for("main.index"))
    # posts = Post.query.all()
    return render_template('contact/index.html', form=contact_form, logged_in=current_user.is_authenticated, user=current_user)

# @bp.route('/categories/')
# def categories():
#     return render_template('posts/categories.html')