# 📝 Secure Notes API

A simple backend API built using Flask for user authentication and notes management.

---

## 🚀 Features

* User Registration
* User Login
* Database Integration (SQLite / SQLAlchemy)
* Deployed on Render

---

## 🛠 Tech Stack

* Python (Flask)
* SQLAlchemy
* Gunicorn
* Render

---

## 🌐 Live API

https://notes-api-sycv.onrender.com

---

## 📌 API Endpoints

### 🔹 Home

**GET /**

```
Response:
{
  "message": "Welcome to the Notes API!"
}
```

---

### 🔹 Register User

**POST /register**

```
Body:
{
  "username": "testuser",
  "password": "123456"
}
```

---

### 🔹 Login User

**POST /login**

```
Body:
{
  "username": "testuser",
  "password": "123456"
}
```

---

## ⚙️ Run Locally

```
git clone <https://github.com/anujsinha1429/SECURE_NOTES_API.git>
cd NOTES_API
pip install -r requirements.txt
python run.py
```

---

## 🚀 Deployment

* Hosted on Render
* Uses Gunicorn as production server

---

## 📌 Future Improvements

* JWT Authentication
* Notes CRUD (Create, Read, Update, Delete)
* Frontend Integration

---

## 👨‍💻 Author

Anuj Sinha 🛐
