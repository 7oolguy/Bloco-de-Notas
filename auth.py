from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from extensions import db

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # Guard clause para métodos que não sejam POST
    if request.method != 'POST':
        return render_template('signup.html')

    # Guard clause para verificar se os campos foram preenchidos
    if not (username := request.form.get('username')) or not (password := request.form.get('password')):
        flash('Nome de usuário e senha são obrigatórios.', 'error')
        return redirect(url_for('auth.signup'))

    # Guard clause para verificar se o usuário já existe
    if User.query.filter_by(username=username).first():
        flash('Usuário já existe. Por favor, escolha outro nome.', 'error')
        return redirect(url_for('auth.signup'))

    # Cria e salva o novo usuário
    new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
    db.session.add(new_user)
    db.session.commit()

    flash('Cadastro realizado com sucesso! Agora você pode fazer login.', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Guard clause para métodos que não sejam POST
    if request.method != 'POST':
        return render_template('login.html')

    # Guard clause para verificar se os campos foram preenchidos
    if not (username := request.form.get('username')) or not (password := request.form.get('password')):
        flash('Nome de usuário e senha são obrigatórios.', 'error')
        return redirect(url_for('auth.login'))

    # Guard clause para verificar usuário e senha
    if not (user := User.query.filter_by(username=username).first()) or not check_password_hash(user.password, password):
        flash('Credenciais inválidas. Por favor, tente novamente.', 'error')
        return redirect(url_for('auth.login'))

    # Realiza o login e redireciona para o dashboard
    login_user(user)
    flash('Login realizado com sucesso!', 'success')
    return redirect(url_for('notes'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
