from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.player import Player

class PlayerService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            player = Player(
                id=data["id"],
                nome=data["nome"],
                pontuacao=data["pontuacao"],
            )
            self.session.add(player)
            self.session.commit()

            # Serializa antes de fechar a sessão
            response = {
                "id": player.id,
                "nome": player.nome,
                "pontuacao": player.pontuacao
            }

            self.session.close()
            return jsonify(response), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        player = self.session.get(Player, id)  # usa get correto

        if not player:
            self.session.close()
            return jsonify({"error": "Player não encontrado"}), 404

        response = {
            "id": player.id,
            "nome": player.nome,
            "pontuacao": player.pontuacao
        }

        self.session.close()
        return jsonify(response)

    def atualizar(self, id):
        data = request.get_json()
        player = self.session.get(Player, id)

        if not player:
            self.session.close()
            return jsonify({"error": "Player não encontrado"}), 404

        if "nome" in data:
            player.nome = data["nome"]
        if "pontuacao" in data:
            player.pontuacao = data["pontuacao"]

        player.modified_at = datetime.now()

        self.session.commit()
        self.session.close()
        return jsonify({"message": "Player atualizado com sucesso"})

    def deletar(self, id):
        player = self.session.get(Player, id)

        if not player:
            self.session.close()
            return jsonify({"error": "Player não encontrado"}), 404

        try:
            self.session.delete(player)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "Player deletado com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify({"message": "Não é possível deletar este player, ele está associado a outras tabelas"}), 401