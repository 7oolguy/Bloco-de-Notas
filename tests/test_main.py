from App.app import db
from models import User, Note

# Criar e testar a conexão com o banco de dados
with app.app_context():
    # Criar as tabelas
    db.create_all()

    # Testar a inserção de um usuário
    new_user = User(username='testuser', password='testpassword')
    db.session.add(new_user)
    db.session.commit()

    # Testar a recuperação do usuário
    user = User.query.filter_by(username='testuser').first()
    print(f"Usuário encontrado: {user.username}" if user else "Usuário não encontrado")
