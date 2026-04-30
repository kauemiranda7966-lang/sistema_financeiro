import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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