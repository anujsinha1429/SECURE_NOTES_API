from flask import Blueprint, request, jsonify

notes= Blueprint('notes', __name__)
@notes.route("/notes",)
def notes_check():
    return jsonify({"message": "This is the notes endpoint!"})