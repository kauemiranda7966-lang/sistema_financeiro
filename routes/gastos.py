from flask import Blueprint, render_template, request, redirect, session
from models.gasto import adicionar_gasto, listar_gastos, deletar_gasto

gastos_bp = Blueprint("gastos", __name__)

@gastos_bp.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect("/")

    gastos = listar_gastos(session["usuario_id"])

    total = sum(g[2] for g in gastos)

    return render_template("dashboard.html", gastos=gastos, total=total)

@gastos_bp.route("/add", methods=["POST"])
def add():
    nome = request.form["nome"]
    valor = request.form["valor"]

    adicionar_gasto(nome, valor, session["usuario_id"])
    return redirect("/dashboard")


@gastos_bp.route("/delete/<int:id>")
def delete(id):
    deletar_gasto(id, session["usuario_id"])
    return redirect("/dashboard")


def atualizar_gasto(id, nome, valor, usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE gastos SET nome=?, valor=? WHERE id=? AND usuario_id=?",
        (nome, valor, id, usuario_id)
    )

    conn.commit()
    conn.close()
