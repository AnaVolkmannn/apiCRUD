from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.fase_service import FaseService

database = DBConnectionHandler()
database.__enter__()
fase_service = FaseService(database)

fases_bp = Blueprint('fases', __name__)


@fases_bp.route("/fases", methods=["POST"])
def criar_fase():
    return fase_service.criar()


@fases_bp.route("/fases/<int:id>", methods=["GET"])
def obter_fase(id):
    return fase_service.obter(id)


@fases_bp.route("/fases/<int:id>", methods=["PUT"])
def atualizar_fase(id):
    return fase_service.atualizar(id)


@fases_bp.route("/fases/<int:id>", methods=["DELETE"])
def deletar_fase(id):
    return fase_service.deletar(id)