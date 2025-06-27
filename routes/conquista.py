from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.conquista_service import ConquistaService

database = DBConnectionHandler()
database.__enter__()
conquista_service = ConquistaService(database)

conquistas_bp = Blueprint('conquistas', __name__)


@conquistas_bp.route("/conquistas", methods=["POST"])
def criar_conquista():
    return conquista_service.criar()


@conquistas_bp.route("/conquistas/<int:id>", methods=["GET"])
def obter_conquista(id):
    return conquista_service.obter(id)


@conquistas_bp.route("/conquistas/<int:id>", methods=["DELETE"])
def deletar_conquista(id):
    return conquista_service.deletar(id)