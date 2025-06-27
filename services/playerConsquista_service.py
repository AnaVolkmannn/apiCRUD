from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.player_conquista import PlayerConquista

class PlayerConquistaService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            player_conquista = PlayerConquista(
                player_id=data["player_id"],
                conquista_id=data["conquista_id"]
            )
            self.session.add(player_conquista)
            self.session.commit()
            self.session.close()

            return jsonify({
                # "id": player_conquista.id,  # se seu model não tiver id, comente essa linha
                "player_id": player_conquista.player_id,
                "conquista_id": player_conquista.conquista_id
            }), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        player_conquista = self.session.get(PlayerConquista, id)
        if not player_conquista:
            self.session.close()
            return jsonify({"error": "PlayerConquista não encontrada"}), 404
        response = {
            # "id": player_conquista.id,  # idem aqui, só se tiver id
            "player_id": player_conquista.player_id,
            "conquista_id": player_conquista.conquista_id
        }
        self.session.close()
        return jsonify(response)

    def deletar(self, id):
        player_conquista = self.session.get(PlayerConquista, id)
        if not player_conquista:
            self.session.close()
            return jsonify({"error": "PlayerConquista não encontrada"}), 404

        try:
            self.session.delete(player_conquista)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "PlayerConquista deletada com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify({"message": "Não é possível deletar esta PlayerConquista, está associada a outras tabelas"}), 401