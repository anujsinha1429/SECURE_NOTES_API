from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    db.init_app(app)
    from app.routes.auth import auth
    from app.routes.notes import notes 
    app.register_blueprint(auth)
    app.register_blueprint(notes)
    return app


