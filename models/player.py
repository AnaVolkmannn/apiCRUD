from sqlalchemy import Column, Integer, String
from infra.base import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    pontuacao = Column(Integer, default=0)

    def __repr__(self):
        return f"Player(id={self.id}, nome='{self.nome}', pontuacao={self.pontuacao})"

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "pontuacao": self.pontuacao}