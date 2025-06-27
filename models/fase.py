from sqlalchemy import Column, Integer, String
from infra.base import Base

class Fase(Base):
    __tablename__ = 'fases'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    ordem = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Fase(id={self.id}, titulo='{self.titulo}', ordem={self.ordem})"