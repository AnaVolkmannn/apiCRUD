from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.playerConsquista_service import PlayerConquistaService

database = DBConnectionHandler()
database.__enter__()
player_conquista_service = PlayerConquistaService(database)

player_conquistas_bp = Blueprint('player_conquistas', __name__)


@player_conquistas_bp.route("/player_conquistas", methods=["POST"])
def criar_player_conquista():
    return player_conquista_service.criar()


@player_conquistas_bp.route("/player_conquistas/<int:id>", methods=["GET"])
def obter_player_conquista(id):
    return player_conquista_service.obter(id)


@player_conquistas_bp.route("/player_conquistas/<int:id>", methods=["DELETE"])
def deletar_player_conquista(id):
    return player_conquista_service.deletar(id)