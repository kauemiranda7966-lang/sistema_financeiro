import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import sqlite3

def conectar():
    return sqlite3.connect("database.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        senha TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        valor REAL,
        usuario_id INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )
    """)

    conn.commit()
    conn.close()

from flask import Flask
from routes.auth import auth
from routes.gastos import gastos_bp
from database.db import criar_tabelas

app = Flask(__name__)
app.secret_key = "segredo"

# criar banco
criar_tabelas()

# registrar rotas
app.register_blueprint(auth)
app.register_blueprint(gastos_bp)

if __name__ == "__main__":
    app.run(debug=True)
