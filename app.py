from flask import Flask, render_template, redirect, url_for, request, flash
from extensions import db
from flask_login import LoginManager
from os import environ
from dotenv import load_dotenv
from flask_login import login_required, current_user

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar a aplicação
app = Flask(__name__)

# Configuração de chave secreta e banco de dados
app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar a extensão SQLAlchemy
db.init_app(app)

# Configurar o gerenciador de login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Registrar blueprints
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from api.notes import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/notes')
@login_required
def notes():
    return render_template('notes.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# Executar o aplicativo e criar tabelas se não existirem
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
