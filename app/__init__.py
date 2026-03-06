from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db= SQLAlchemy()
login_manager = LoginManager()

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
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


