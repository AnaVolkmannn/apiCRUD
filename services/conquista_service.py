from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from models.conquista import Conquista

class ConquistaService:
    def __init__(self, database):
        self.session = database.session

    def criar(self):
        data = request.get_json()
        try:
            conquista = Conquista(
                nome=data["nome"],
                descricao=data["descricao"],
                pontos=data["pontos"]
            )
            self.session.add(conquista)
            self.session.commit()

            response = {
                "id": conquista.id,
                "nome": conquista.nome,
                "descricao": conquista.descricao,
                "pontos": conquista.pontos
            }

            self.session.close()
            return jsonify(response), 201
        except Exception as e:
            self.session.rollback()
            self.session.close()
            return jsonify({"error": str(e)}), 400

    def obter(self, id):
        conquista = self.session.get(Conquista, id)
        if not conquista:
            self.session.close()
            return jsonify({"error": "Conquista não encontrada"}), 404

        response = {
            "id": conquista.id,
            "nome": conquista.nome,
            "descricao": conquista.descricao,
            "pontos": conquista.pontos
        }
        self.session.close()
        return jsonify(response)

    def atualizar(self, id):
        data = request.get_json()
        conquista = self.session.get(Conquista, id)
        if not conquista:
            self.session.close()
            return jsonify({"error": "Conquista não encontrada"}), 404

        if "nome" in data:
            conquista.nome = data["nome"]
        if "descricao" in data:
            conquista.descricao = data["descricao"]
        if "pontos" in data:
            conquista.pontos = data["pontos"]

        conquista.modified_at = datetime.now()

        self.session.commit()
        self.session.close()
        return jsonify({"message": "Conquista atualizada com sucesso"})

    def deletar(self, id):
        conquista = self.session.get(Conquista, id)
        if not conquista:
            self.session.close()
            return jsonify({"error": "Conquista não encontrada"}), 404

        try:
            self.session.delete(conquista)
            self.session.commit()
            self.session.close()
            return jsonify({"message": "Conquista deletada com sucesso"})
        except IntegrityError:
            self.session.rollback()
            self.session.close()
            return jsonify({"message": "Não é possível deletar esta conquista, está associada a outras tabelas"}), 401