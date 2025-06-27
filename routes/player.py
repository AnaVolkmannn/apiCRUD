from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.player_service import PlayerService

database = DBConnectionHandler()
database.__enter__()
player_service = PlayerService(database)

players_bp = Blueprint('players', __name__)


@players_bp.route("/players", methods=["POST"])
def criar_player():
    return player_service.criar()


@players_bp.route("/players/<int:id>", methods=["GET"])
def obter_player(id):
    return player_service.obter(id)


@players_bp.route("/players/<int:id>", methods=["PUT"])
def atualizar_player(id):
    return player_service.atualizar(id)


@players_bp.route("/players/<int:id>", methods=["DELETE"])
def deletar_player(id):
    return player_service.deletar(id)