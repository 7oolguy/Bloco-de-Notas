from flask import Blueprint, request, jsonify
from models import Note
from extensions import db
from sqlalchemy.exc import SQLAlchemyError

api = Blueprint('api', __name__)

@api.route('/notes', methods=['GET'])
def get_notes():
    """Obtém todas as notas."""
    try:
        # Busca todas as notas
        notes = Note.query.all()
        # Retorna uma lista de notas no formato JSON
        return jsonify([{"id": note.id, "title": note.title, "content": note.content} for note in notes]), 200
    except SQLAlchemyError as e:
        # Em caso de erro no banco de dados, retorna erro 500 com detalhes
        return jsonify({"error": "Falha ao recuperar as notas", "details": str(e)}), 500
    
@api.route('/notes/<int:note_id>', methods=['GET'])
def get_singleNote(note_id):
    """Obtém uma nota específica pelo ID."""
    try:
        # Busca uma nota pelo ID
        note = Note.query.get(note_id)
        if note is None:
            # Retorna erro 404 se a nota não for encontrada
            return jsonify({"error": "Nota não encontrada"}), 404
        # Retorna a nota no formato JSON
        return jsonify({"id": note.id, "title": note.title, "content": note.content}), 200
    except SQLAlchemyError as e:
        # Em caso de erro no banco de dados, retorna erro 500 com detalhes
        return jsonify({"error": "Falha ao recuperar a nota", "details": str(e)}), 500
    
@api.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    """Obtém uma nota específica pelo ID."""
    try:
        # Busca uma nota pelo ID
        note = Note.query.get(note_id)
        if note is None:
            # Retorna erro 404 se a nota não for encontrada
            return jsonify({"error": "Nota não encontrada"}), 404
        # Retorna a nota no formato JSON
        return jsonify({"id": note.id, "title": note.title, "content": note.content}), 200
    except SQLAlchemyError as e:
        # Em caso de erro no banco de dados, retorna erro 500 com detalhes
        return jsonify({"error": "Falha ao recuperar a nota", "details": str(e)}), 500
@api.route('/notes', methods=['POST'])
def create_note():
    """Cria uma nova nota."""
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    # Validação de dados: título e conteúdo são obrigatórios
    if not title or not content:
        return jsonify({"error": "Título e conteúdo são obrigatórios"}), 400

    new_note = Note(title=title, content=content)
    try:
        # Adiciona e confirma a nova nota no banco de dados
        db.session.add(new_note)
        db.session.commit()
        # Retorna mensagem de sucesso e o ID da nova nota
        return jsonify({"message": "Nota criada com sucesso", "id": new_note.id}), 201
    except SQLAlchemyError as e:
        # Em caso de erro, faz rollback e retorna erro 500 com detalhes
        db.session.rollback()
        return jsonify({"error": "Falha ao criar nota", "details": str(e)}), 500

@api.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    """Atualiza uma nota existente."""
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    try:
        # Busca a nota pelo ID
        note = Note.query.get(note_id)
        if note is None:
            # Retorna erro 404 se a nota não for encontrada
            return jsonify({"error": "Nota não encontrada"}), 404

        # Atualiza título e/ou conteúdo se eles forem fornecidos
        if title:
            note.title = title
        if content:
            note.content = content

        db.session.commit()
        # Retorna mensagem de sucesso
        return jsonify({"message": "Nota atualizada com sucesso"}), 200
    except SQLAlchemyError as e:
        # Em caso de erro, faz rollback e retorna erro 500 com detalhes
        db.session.rollback()
        return jsonify({"error": "Falha ao atualizar nota", "details": str(e)}), 500
@api.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Deleta uma nota específica pelo ID."""
    try:
        # Busca a nota pelo ID
        note = Note.query.get(note_id)
        if note is None:
            # Retorna erro 404 se a nota não for encontrada
            return jsonify({"error": "Nota não encontrada"}), 404

        # Deleta a nota e confirma no banco de dados
        db.session.delete(note)
        db.session.commit()
        # Retorna mensagem de sucesso
        return jsonify({"message": "Nota deletada com sucesso"}), 200
    except SQLAlchemyError as e:
        # Em caso de erro, faz rollback e retorna erro 500 com detalhes
        db.session.rollback()
        return jsonify({"error": "Falha ao deletar nota", "details": str(e)}), 500
    
