from flask import Blueprint, request, jsonify,session
from werkzeug.security import generate_password_hash,check_password_hash
from app.models import User
from app import db

auth= Blueprint('auth', __name__)
 
@auth.route("/")
def home():
    return jsonify({"message": "Welcome to the Notes API!"})

@auth.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    hashed_password=generate_password_hash(password)
    # Here you would typically save the user to the database
    user=User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@auth.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    # Here you would typically check the username and password against the database
    user=User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session["user_id"]=user.id
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid username or password!"}), 401