from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.interacao_npc import InteracaoNPC

class InteracaoNPCService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            interacao = InteracaoNPC(
                player_id=data["player_id"],
                npc_id=data["npc_id"],
                data=data["data"]  # campo data (assumido no model)
            )
            self.session.add(interacao)
            self.session.commit()

            response = {
                "id": interacao.id,
                "player_id": interacao.player_id,
                "npc_id": interacao.npc_id,
                "data": interacao.data.strftime('%Y-%m-%d %H:%M:%S') if interacao.data else None
            }

            self.session.close()
            return jsonify(response), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        interacao = self.session.get(InteracaoNPC, id)
        if not interacao:
            self.session.close()
            return jsonify({"error": "Interação não encontrada"}), 404

        response = {
            "id": interacao.id,
            "player_id": interacao.player_id,
            "npc_id": interacao.npc_id,
            "data": interacao.data.strftime('%Y-%m-%d %H:%M:%S') if interacao.data else None
        }

        self.session.close()
        return jsonify(response)

    def atualizar(self, id):
        data = request.get_json()
        interacao = self.session.get(InteracaoNPC, id)
        if not interacao:
            self.session.close()
            return jsonify({"error": "Interação não encontrada"}), 404

        if "player_id" in data:
            interacao.player_id = data["player_id"]
        if "npc_id" in data:
            interacao.npc_id = data["npc_id"]
        if "data" in data:
            interacao.data = data["data"]

        interacao.modified_at = datetime.now()

        self.session.commit()
        self.session.close()
        return jsonify({"message": "Interação atualizada com sucesso"})

    def deletar(self, id):
        interacao = self.session.get(InteracaoNPC, id)
        if not interacao:
            self.session.close()
            return jsonify({"error": "Interação não encontrada"}), 404

        try:
            self.session.delete(interacao)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "Interação deletada com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify({"message": "Não é possível deletar esta interação, está associada a outras tabelas"}), 401