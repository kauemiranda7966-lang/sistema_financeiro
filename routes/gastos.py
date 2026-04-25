from flask import Blueprint, render_template, request, redirect, session

from models.gasto import (
    adicionar_gasto,
    listar_gastos,
    deletar_gasto,
    atualizar_gasto,
    buscar_gasto_por_id
)

gastos_bp = Blueprint("gastos", __name__)


@gastos_bp.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect("/")

    gastos = listar_gastos(session["usuario_id"])
    total = sum(float(g[2]) for g in gastos)
    
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


@gastos_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "usuario_id" not in session:
        return redirect("/")

    if request.method == "POST":
        nome = request.form["nome"]
        valor = request.form["valor"]

        atualizar_gasto(id, nome, valor, session["usuario_id"])
        return redirect("/dashboard")

    gasto = buscar_gasto_por_id(id, session["usuario_id"])

    return render_template("edit.html", gasto=gasto)