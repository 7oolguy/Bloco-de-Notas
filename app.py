from flask import Flask, render_template, redirect, url_for, request, flash
from extensions import db
from os import environ
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar a aplicação
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializar a extensão SQLAlchemy
db.init_app(app)
from api.notes import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/')
def notes():
    return render_template('notes.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5001)
