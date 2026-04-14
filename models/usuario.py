from database.db import conectar

def criar_usuario(username, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (username, senha) VALUES (?, ?)",
        (username, senha)
    )

    conn.commit()
    conn.close()


def buscar_usuario(username, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE username=? AND senha=?",
        (username, senha)
    )

    usuario = cursor.fetchone()
    conn.close()

    return usuario