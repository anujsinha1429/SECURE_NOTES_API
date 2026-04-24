from flask import Flask 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db= SQLAlchemy()
login_manager = LoginManager()

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)
    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    from app.routes.auth import auth
    from app.routes.notes import notes 
    app.register_blueprint(auth)
    app.register_blueprint(notes)
    return app


