from sqlalchemy import Column, Integer, String
from infra.base import Base

class Conquista(Base):
    __tablename__ = 'conquistas'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)

    def __repr__(self):
        return f"Conquista(id={self.id}, descricao='{self.descricao}')"