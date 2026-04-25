from flask import Blueprint, render_template, request, redirect, session
from models.usuario import criar_usuario, buscar_usuario

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]

        usuario = buscar_usuario(username, senha)

        if usuario:
            session["usuario_id"] = usuario[0]
            return redirect("/dashboard")

    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]

        criar_usuario(username, senha)
        return redirect("/")

    return render_template("register.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]

        if len(username) < 3:
            return "Usuário muito curto"

        if len(senha) < 4:
            return "Senha muito fraca"

        criar_usuario(username, senha)
        return redirect("/")

    return render_template("register.html")