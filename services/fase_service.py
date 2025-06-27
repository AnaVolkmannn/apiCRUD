from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.fase import Fase

class FaseService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            fase = Fase(
                titulo=data["titulo"],
                ordem=data["ordem"],
            )
            self.session.add(fase)
            self.session.commit()

            response = {
                "id": fase.id,
                "titulo": fase.titulo,
                "ordem": fase.ordem
            }

            self.session.close()
            return jsonify(response), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        fase = self.session.get(Fase, id)
        if not fase:
            self.session.close()
            return jsonify({"error": "Fase não encontrada"}), 404

        response = {
            "id": fase.id,
            "titulo": fase.titulo,
            "ordem": fase.ordem
        }

        self.session.close()
        return jsonify(response)

    def atualizar(self, id):
        data = request.get_json()
        fase = self.session.get(Fase, id)
        if not fase:
            self.session.close()
            return jsonify({"error": "Fase não encontrada"}), 404

        if "titulo" in data:
            fase.titulo = data["titulo"]
        if "ordem" in data:
            fase.ordem = data["ordem"]

        fase.modified_at = datetime.now()

        self.session.commit()
        self.session.close()
        return jsonify({"message": "Fase atualizada com sucesso"})

    def deletar(self, id):
        fase = self.session.get(Fase, id)
        if not fase:
            self.session.close()
            return jsonify({"error": "Fase não encontrada"}), 404

        try:
            self.session.delete(fase)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "Fase deletada com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify({"message": "Não é possível deletar esta fase, está associada a outras tabelas"}), 401