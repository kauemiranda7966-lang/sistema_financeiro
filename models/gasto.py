from database.db import conectar

def adicionar_gasto(nome, valor, usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO gastos (nome, valor, usuario_id) VALUES (?, ?, ?)",
        (nome, valor, usuario_id)
    )

    conn.commit()
    conn.close()


def listar_gastos(usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM gastos WHERE usuario_id=?",
        (usuario_id,)
    )

    gastos = cursor.fetchall()
    conn.close()

    return gastos


def deletar_gasto(id_gasto, usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM gastos WHERE id=? AND usuario_id=?",
        (id_gasto, usuario_id)
    )

    conn.commit()
    conn.close()


# ✅ FORA de qualquer função
def atualizar_gasto(id_gasto, nome, valor, usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE gastos SET nome=?, valor=? WHERE id=? AND usuario_id=?",
        (nome, valor, id_gasto, usuario_id)
    )

    conn.commit()
    conn.close()


# ✅ FORA também
def buscar_gasto_por_id(id_gasto, usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM gastos WHERE id=? AND usuario_id=?",
        (id_gasto, usuario_id)
    )

    gasto = cursor.fetchone()
    conn.close()

    return gasto