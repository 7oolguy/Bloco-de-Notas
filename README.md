# Bloco de Notas

Um aplicativo web de anotações desenvolvido com Flask, Oracle SQL e uma API RESTful. Permite que usuários se cadastrem, façam login e gerenciem suas notas através de uma interface intuitiva. Ideal para quem deseja organizar suas anotações de maneira segura e eficiente.

## Funcionalidades

- **Autenticação de Usuário**: Login e registro seguros usando Flask-Login e Flask-Bcrypt.
- **Operações CRUD**: Criar, Ler, Atualizar e Deletar notas via uma API RESTful.
- **Banco de Dados Oracle SQL**: Armazena dados de usuários e notas.
- **Design Responsivo**: Otimizado para visualização em desktops e dispositivos móveis.

## Stack Tecnológico

- **Backend**: Flask, Flask-RESTful
- **Banco de Dados**: Oracle SQL (usando a extensão Oracle SQL do VS Code)
- **Frontend**: HTML, CSS, JavaScript (AJAX para chamadas à API)
- **Autenticação**: Flask-Login, Flask-Bcrypt para manipulação segura de senhas

## Pré-requisitos

- Python 3.7+
- Oracle SQL (usando a extensão Oracle SQL no VS Code)
- Visual Studio Code (recomendado)

## Começando

### 1. Clone o Repositório

```bash
git clone https://github.com/7oolguy/Bloco-de-Notas.git
cd Bloco-de-Notas
```

# Instale as Dependências

Instale os pacotes Python necessários listados em **requirements.txt**

```bash
pip install -r requirements.txt
```

# Configure as variáveis de Ambiente

Crie um Arquivo **.env** no diretório raiz do projeto com as seguintes configurações

```bash
SECRET_KEY='sua_chave_secreta'
SQLALCHEMY_DATABASE_URI='oracle+oracledb://usuario:senha@host_do_banco:porta/nome_do_banco'
```

Substitua os placeholders com suas credenciais reais do banco de dados e uma chave secreta segura

# Inicialize o Banco de Dados

Abra um shell Python e execute

```bash
from app import db
db.create_all()
```

# Execute o aplicativo

```bash
flask run
```

O app vai rodar em **http://127.0.0.1:5000**

# Uso

- Acesse **/auth/signup** para criar uma nova conta
- Faça login em **/auth/login** para acessar o painel principal de notas
- Use o painel para criar, visualizar, editar e deletar suas notas

## Endpoints API

Os seguintes endpoints de API estão disponiveis para o gerenciamento de notas:

- **GET /api/notes** - Recupera todas as notas do usuário logado.
- **GET /api/notes/<note_id>** - Recupera uma nota especifica utilizando o ID
- **POST /api/notes** - Cria uma nova nota.
- **PUT /api/notes/<note_id>** - Atualiza uma nota existente.
- **DELETE /api/notes/<note_id>** - Deleta uma nota.
