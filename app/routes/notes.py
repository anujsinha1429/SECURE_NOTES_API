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
    if not title or not content:
        return jsonify({"message": "Title and content are required!"}), 400

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

@notes.route("/notes/<int:id>",methods=["DELETE"])
@login_required
def delete_note(id):
    note=Note.query.filter_by(id=id,user_id=current_user.id).first()
    if not note:
        return jsonify({"message":"Note not found!"}),404
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message":"note deleted successfully!"})

@notes.route("/notes/<int:id>",methods=["PUT"])
@login_required
def update_note(id):
    note=Note.query.filter_by(id=id,user_id=current_user.id).first()
    if not note:
        return jsonify({"message":"note not found!"}),404   
    data= request.get_json()
    note.title= data.get("title",note.title)
    note.content= data.get("content",note.content)
    db.session.commit()
    return jsonify({"message":"note updated successfully!"})


