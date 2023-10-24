from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_gravatar import Gravatar
from flask_login import LoginManager, current_user, logout_user
from app.models.user import User
# from flask_login import LoginManager
from config import Config
from app.extensions import db
from forms import RegisterForm, LoginForm


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    Bootstrap(app)
    # login_manager = LoginManager()
    # login_manager.init_app(app)

    # Initialize Flask extensions here
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # login_form = LoginForm()

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    gravatar = Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        force_lower=False,
                        use_ssl=False,
                        base_url=None)



    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.login import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    from app.register import bp as register_bp
    app.register_blueprint(register_bp, url_prefix='/register')

    from app.contact import bp as contact_bp
    app.register_blueprint(contact_bp, url_prefix='/contact')

    # from app.register import bp as logout_bp
    # app.register_blueprint(logout_bp, url_prefix='/logout')

    # from app.questions import bp as questions_bp
    # app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    @app.route('/logout/')
    def logout():
        if current_user:
            logout_user()
        return redirect(url_for('main.index'))

    return app
