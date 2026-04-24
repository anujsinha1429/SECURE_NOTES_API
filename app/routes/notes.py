from flask import Blueprint, request, jsonify,session
from flask_login import login_required, current_user
from app.models import Note
from app import db
from sqlalchemy import or_


notes= Blueprint('notes', __name__)

@notes.route("/notes",methods=["POST"])
@login_required
def notes_created():
    data= request.get_json()
    title= data.get("title")
    content= data.get("content")
    if not title or not content:
        return jsonify({"status":"error",
            "message": "Title and content are required!"}), 400

    note = Note(title=title,content=content, user_id=current_user.id)
    db.session.add(note)
    db.session.commit()
    return jsonify({"status": "success",
                    "data":{
                        "id":note.id,
                        "tittle": note.title,
                        "content":note.content
                        
                    }
                    })

@notes.route("/notes",methods=["GET"])
@login_required
def get_notes():
    search =request.args.get("search","",type=str)
    notes_query= Note.query.filter_by(user_id=current_user.id)
    if search:
        notes_query=notes_query.filter(
            or_(
                Note.title.ilike(f"%{search}%"),
                Note.content.ilike(f"%{search}%")
        ))

    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 5, type=int)

    
    notes=notes_query.offset((page-1)*limit).limit(limit).all()
    

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



