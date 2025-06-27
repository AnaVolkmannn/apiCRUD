from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.interacaoNPC_service import InteracaoNPCService

database = DBConnectionHandler()
database.__enter__()
interacao_service = InteracaoNPCService(database)

interacoes_bp = Blueprint('interacoes', __name__)


@interacoes_bp.route("/interacoes", methods=["POST"])
def criar_interacao():
    return interacao_service.criar()


@interacoes_bp.route("/interacoes/<int:id>", methods=["GET"])
def obter_interacao(id):
    return interacao_service.obter(id)


@interacoes_bp.route("/interacoes/<int:id>", methods=["DELETE"])
def deletar_interacao(id):
    return interacao_service.deletar(id)