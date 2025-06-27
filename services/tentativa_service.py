from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.tentativa import Tentativa
from datetime import datetime

class TentativaService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            tentativa = Tentativa(
                player_id=data["player_id"],
                numero_tentativas=data["numero_tentativas"],
                tempo_resolucao=data["tempo"],  # aqui o nome correto do atributo
                modalidade=data["modalidade"],
                pontuacao_obtida=data["pontuacao"]  # nome real do atributo
            )
            self.session.add(tentativa)
            self.session.commit()
            self.session.close()

            return jsonify({
                "id": tentativa.id,
                "player_id": tentativa.player_id,
                "numero_tentativas": tentativa.numero_tentativas,
                "tempo": tentativa.tempo_resolucao,
                "modalidade": tentativa.modalidade,
                "pontuacao": tentativa.pontuacao_obtida
            }), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        tentativa = self.session.get(Tentativa, id)
        if not tentativa:
            self.session.close()
            return jsonify({"error": "Tentativa não encontrada"}), 404

        response = {
            "id": tentativa.id,
            "player_id": tentativa.player_id,
            "numero_tentativas": tentativa.numero_tentativas,
            "tempo": tentativa.tempo_resolucao,
            "modalidade": tentativa.modalidade,
            "pontuacao": tentativa.pontuacao_obtida
        }
        self.session.close()
        return jsonify(response)

    def deletar(self, id):
        tentativa = self.session.get(Tentativa, id)
        if not tentativa:
            self.session.close()
            return jsonify({"error": "Tentativa não encontrada"}), 404

        try:
            self.session.delete(tentativa)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "Tentativa deletada com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify(
                {"message": "Não é possível deletar este item, ele está associado a outras tabelas"}
            ), 401