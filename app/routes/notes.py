from flask import Blueprint, request, jsonify,session
from flask_login import login_required, current_user
from app.models import Note
from app import db


notes= Blueprint('notes', __name__)
@notes.route("/notes",methods=["POST"])

@login_required
def notes_check():
    data= request.get_json()
    title= data.get("title")
    content= data.get("content")

    note = Note(title=title,content=content, user_id=current_user.id)
    db.session.add(note)
    db.session.commit()
    return jsonify({"message": "Note created successfully!"})

@notes.route("/notes",methods=["GET"])
@login_required
def get_notes():
    notes= Note.query.filter_by(user_id=current_user.id).all()
    results= []
    for note in notes:
        results.append({
            "id": note.id,
            "title": note.title,
            "content": note.content
        })
    return jsonify(results)
