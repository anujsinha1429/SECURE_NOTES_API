from flask import Blueprint, request, jsonify,session
from flask_login import login_user
from werkzeug.security import generate_password_hash,check_password_hash
from app.models import User
from app import db
from flask_login import logout_user
from flask_login import login_required

auth= Blueprint('auth', __name__)
 
@auth.route("/")
def home():
    return jsonify({"message": "Welcome to the Notes API!"})




@auth.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
       return jsonify({"error": "Username already exists"}), 400
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
        login_user(user)
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid username or password!"}), 401


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})



