from flask import Flask
from routes.conquista import conquistas_bp
from routes.fase import fases_bp
from routes.interacao_npc import interacoes_bp
from routes.npc import npcs_bp
from routes.player_conquista import player_conquistas_bp
from routes.player import players_bp
from routes.progresso import progresso_bp
from routes.tentativa import tentativas_bp

from infra.dbconnection import DBConnectionHandler
from infra.base import Base

database = DBConnectionHandler()

try:
    # Cria tabelas no banco se não existirem
    Base.metadata.create_all(database.get_engine())

    app = Flask(__name__)

    # Registra as rotas no app
    app.register_blueprint(conquistas_bp)
    app.register_blueprint(fases_bp)
    app.register_blueprint(interacoes_bp)
    app.register_blueprint(npcs_bp)
    app.register_blueprint(player_conquistas_bp)
    app.register_blueprint(players_bp)
    app.register_blueprint(progresso_bp)
    app.register_blueprint(tentativas_bp)

except Exception as e:
    print("\nBanco de dados desconectado...")
    print(e)

if __name__ == "__main__":
    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=5000, debug=True)