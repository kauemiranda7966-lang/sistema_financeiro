#  Sistema Financeiro com Login (Flask + SQLite)

##  Sobre o Projeto

Este é um sistema web desenvolvido com **Python e Flask** que permite:

* Cadastro de usuários 
* Login e autenticação 
* Controle de gastos individual 

Cada usuário possui seu próprio controle de gastos, garantindo organização e privacidade dos dados.

---

##  Funcionalidades

*  Cadastro de usuários
*  Login e logout
*  Adicionar gastos
*  Listar gastos por usuário
*  Excluir gastos
*  Sessão de usuário (login persistente)

---

##  Tecnologias Utilizadas

* Python
* Flask
* SQLite
* HTML (Jinja2)
* CSS

---

##  Estrutura do Projeto

```
sistema_financeiro/
│
├── app.py
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── models/
│   ├── __init__.py
│   ├── usuario.py
│   └── gasto.py
│
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   └── gastos.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   └── css/
│       └── style.css
│
└── database.db
```

---

##  Como Executar o Projeto

### 1. Clone o repositório

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acesse a pasta

```
cd sistema_financeiro
```

### 3. Instale as dependências

```
pip install flask
```

### 4. Execute o projeto

```
python app.py
```

### 5. Acesse no navegador

```
http://127.0.0.1:5000
```

---

##  Como Funciona a Autenticação

* O usuário faz login com username e senha
* Os dados são verificados no banco SQLite
* A sessão é armazenada usando `session` do Flask
* Cada ação é vinculada ao `usuario_id`

---

##  Conceitos Aplicados

* Separação de responsabilidades
* Estrutura modular (models, routes, database)
* CRUD (Create, Read, Update, Delete)
* Sessões com Flask
* Relacionamento entre tabelas (usuário → gastos)

---

##  Melhorias Futuras

*  Criptografia de senha
*  Edição de gastos
*  Relatórios e gráficos
*  Interface com Bootstrap
*  Deploy na web

---

## 👨 Autor

Desenvolvido por **Kauê Miranda**

---

##  Licença

Este projeto é para fins de estudo e aprendizado.
