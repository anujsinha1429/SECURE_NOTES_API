# 📝 Notes API (Flask)

A simple **Notes API** built using **Python Flask**.  
Users can register, login and create personal notes.  
This project is part of my **#100DaysOfCode journey** where I am learning backend development by building real projects.

---

## 🚀 Features (Currently Implemented)

- User Registration
- User Login (Authentication)
- Create Notes
- Get User Notes
- User specific data using Flask-Login
- Password hashing for security

More features like **Update Notes and Delete Notes** will be added soon.

---

## 🛠 Tech Stack

- Python
- Flask
- Flask-Login
- SQLAlchemy
- SQLite
- Werkzeug (Password Hashing)

---

## 📂 Project Structure

```
NOTES_API
│
├── app
│   ├── routes
│   │   ├── auth.py
│   │   └── notes.py
│   │
│   ├── models.py
│   └── __init__.py
│
├── instance
│
├── run.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

Clone the repository


git clone https://github.com/anujsinha1429/SECURE_NOTES_API.git


Go into the project directory.


cd NOTES_API


Install dependencies

```
pip install -r requirements.txt
```

Run the server

```
python3 run.py (for mac)
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### Register User
```
POST /register
```

Body

```
{
 "username": "anuj",
 "password": "1234"
}
```

---

### Login
```
POST /login
```

Body

```
{
 "username": "anuj",
 "password": "1234"
}
```

---

### Create Note
```
POST /notes
```

Body

```
{
 "title": "study",
 "content": "learn backend"
}
```

---

### Get Notes
```
GET /notes
```

Returns all notes for the logged-in user.

---

## 📚 What I Learned

- Flask Application Factory
- Blueprints
- Authentication using Flask-Login
- SQLAlchemy ORM
- Backend project structure
- REST API basics

---

## 👨‍💻 Author

**Anuj Kumar Sinha**

1st Year Student | Aspiring Backend Developer  
Python • Flask • Backend Development