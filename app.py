from flask import Flask, request, jsonify, render_template
import api.notes as n

# Na linha de comando execute:  flask --app news_service run
app = Flask(__name__)

@app.route('/', methods=['GET'])
def db_info():
    print(jsonify(n.get_db_info()))
    return render_template('notes.html')

@app.route('/notas/', methods=['POST'])
def notas_create():
    try:
        notas = request.get_json()
        return jsonify(n.create(notas))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/notas/<int:note_id>', methods=['GET'])
def notas_read(note_id):  # Change 'id' to 'note_id'
    notas = {"id": note_id}
    return jsonify(n.read(notas))

@app.route('/notas/<int:note_id>', methods=['PUT'])
def notas_update(note_id):  # Change 'id' to 'note_id'
    notas = request.get_json()
    notas["id"] = note_id
    return jsonify(n.update(notas))

@app.route('/notas/<int:note_id>', methods=['DELETE'])
def notas_delete(note_id):  # Change 'id' to 'note_id'
    notas = {"id": note_id}
    return jsonify(n.delete(notas))
