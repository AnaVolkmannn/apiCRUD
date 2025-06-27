from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.npc import NPC

class NPCService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            npc = NPC(
                nome=data["nome"],
                funcao=data["funcao"],
                localizacao=data["localizacao"]
            )
            self.session.add(npc)
            self.session.commit()
            response = {
                "id": npc.id,
                "nome": npc.nome,
                "funcao": npc.funcao,
                "localizacao": npc.localizacao
            }
            self.session.close()
            return jsonify(response), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        npc = self.session.get(NPC, id)
        if not npc:
            self.session.close()
            return jsonify({"error": "NPC não encontrado"}), 404

        response = {
            "id": npc.id,
            "nome": npc.nome,
            "funcao": npc.funcao,
            "localizacao": npc.localizacao
        }
        self.session.close()
        return jsonify(response)

    def atualizar(self, id):
        data = request.get_json()
        npc = self.session.get(NPC, id)
        if not npc:
            self.session.close()
            return jsonify({"error": "NPC não encontrado"}), 404

        if "nome" in data:
            npc.nome = data["nome"]
        if "funcao" in data:
            npc.funcao = data["funcao"]
        if "localizacao" in data:
            npc.localizacao = data["localizacao"]

        npc.modified_at = datetime.now()

        self.session.commit()
        self.session.close()
        return jsonify({"message": "NPC atualizado com sucesso"})

    def deletar(self, id):
        npc = self.session.get(NPC, id)
        if not npc:
            self.session.close()
            return jsonify({"error": "NPC não encontrado"}), 404

        try:
            self.session.delete(npc)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "NPC deletado com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify({"message": "Não é possível deletar este NPC, ele está associado a outras tabelas"}), 401