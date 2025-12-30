from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from .extension import db, jwt
from .presentation.auth import auth_bp

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testuser.db'
    app.secret_key = 'SECRET'
    app.config['SECRET_KEY'] = 'SECRET'

    db.init_app(app)
    jwt.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix="/auth")

    with app.app_context():
        db.create_all()

    return app