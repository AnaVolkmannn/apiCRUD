from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.progresso_service import ProgressoService

database = DBConnectionHandler()
database.__enter__()
progresso_service = ProgressoService(database)

progresso_bp = Blueprint('progresso', __name__)


@progresso_bp.route("/progresso", methods=["POST"])
def criar_progresso():
    return progresso_service.criar()


@progresso_bp.route("/progresso/<int:id>", methods=["GET"])
def obter_progresso(id):
    return progresso_service.obter(id)


@progresso_bp.route("/progresso/<int:id>", methods=["DELETE"])
def deletar_progresso(id):
    return progresso_service.deletar(id)