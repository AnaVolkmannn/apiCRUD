from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.tentativa_service import TentativaService

database = DBConnectionHandler()
database.__enter__()
tentativa_service = TentativaService(database)

tentativas_bp = Blueprint('tentativas', __name__)


@tentativas_bp.route("/tentativas", methods=["POST"])
def criar_tentativa():
    return tentativa_service.criar()


@tentativas_bp.route("/tentativas/<int:id>", methods=["GET"])
def obter_tentativa(id):
    return tentativa_service.obter(id)


@tentativas_bp.route("/tentativas/<int:id>", methods=["DELETE"])
def deletar_tentativa(id):
    return tentativa_service.deletar(id)