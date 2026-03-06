from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    notes=db.relationship('Note', backref='user', lazy=True)

class Note(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(150), nullable=False)
    content= db.Column(db.Text, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



