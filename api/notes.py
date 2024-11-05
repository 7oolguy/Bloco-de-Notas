from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import Note
from app import db

api = Blueprint('api', __name__)

@api.route('/notes', methods=['GET'])
@login_required
def get_notes():
    #Get notes for the logged - in
    ...

@api.route('/notes/<int:note_id>', methods=['GET'])
@login_required
def get_note(note_id):
    # Get note by id
    ...

@api.route('/notes', methods=['POST'])
@login_required
def create_note():
    #Create a new note for the logged-in user
    ...

@api.route('/notes/<int:note_id>', methods=['PUT'])
@login_required
def update_note(note_id):
    # Update an existing note for the logged-in user
    ...

@api.route('/notes/<int:note_id>', methods=['DELETE'])
@login_required
def delete_note(note_id):
    # Delete
    ...
