from sqlalchemy import Column, Integer, String
from infra.base import Base

class NPC(Base):
    __tablename__ = 'npcs'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    funcao = Column(String(100), nullable=False)
    localizacao = Column(String(100), nullable=False)

    def __repr__(self):
        return (
            f"NPC(id={self.id}, nome='{self.nome}', "
            f"funcao='{self.funcao}', localizacao='{self.localizacao}')"
        )