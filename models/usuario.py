from database.db import conectar
from werkzeug.security import generate_password_hash, check_password_hash


def criar_usuario(username, senha):
    conn = conectar()
    cursor = conn.cursor()

    senha_hash = generate_password_hash(senha)

    cursor.execute(
        "INSERT INTO usuarios (username, senha) VALUES (?, ?)",
        (username, senha_hash)
    )

    conn.commit()
    conn.close()


def buscar_usuario(username, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE username=?",
        (username,)
    )

    usuario = cursor.fetchone()
    conn.close()

    # 🔐 valida senha com hash
    if usuario and check_password_hash(usuario[2], senha):
        return usuario

    return None