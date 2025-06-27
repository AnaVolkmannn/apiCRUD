from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.progresso import Progresso

class ProgressoService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            progresso = Progresso(
                player_id=data["player_id"],
                fase_id=data["fase_id"],
                data_progresso=data["data"]  # assumindo o nome correto do campo na model
            )
            self.session.add(progresso)
            self.session.commit()
            self.session.close()

            return jsonify({
                "id": progresso.id,
                "player_id": progresso.player_id,
                "fase_id": progresso.fase_id,
                "data": progresso.data_progresso.strftime('%Y-%m-%d %H:%M:%S') if progresso.data_progresso else None
            }), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        progresso = self.session.get(Progresso, id)
        if not progresso:
            self.session.close()
            return jsonify({"error": "Progresso não encontrado"}), 404
        response = {
            "id": progresso.id,
            "player_id": progresso.player_id,
            "fase_id": progresso.fase_id,
            "data": progresso.data_progresso.strftime('%Y-%m-%d %H:%M:%S') if progresso.data_progresso else None
        }
        self.session.close()
        return jsonify(response)

    def deletar(self, id):
        progresso = self.session.get(Progresso, id)
        if not progresso:
            self.session.close()
            return jsonify({"error": "Progresso não encontrado"}), 404
        try:
            self.session.delete(progresso)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "Progresso deletado com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify({"message": "Não é possível deletar este progresso, está associado a outras tabelas"}), 401