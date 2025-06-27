from flask import Blueprint
from infra.dbconnection import DBConnectionHandler
from services.npc_service import NPCService

database = DBConnectionHandler()
database.__enter__()
npc_service = NPCService(database)

npcs_bp = Blueprint('npcs', __name__)


@npcs_bp.route("/npcs", methods=["POST"])
def criar_npc():
    return npc_service.criar()


@npcs_bp.route("/npcs/<int:id>", methods=["GET"])
def obter_npc(id):
    return npc_service.obter(id)


@npcs_bp.route("/npcs/<int:id>", methods=["PUT"])
def atualizar_npc(id):
    return npc_service.atualizar(id)


@npcs_bp.route("/npcs/<int:id>", methods=["DELETE"])
def deletar_npc(id):
    return npc_service.deletar(id)