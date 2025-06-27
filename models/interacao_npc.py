from sqlalchemy import Column, Integer, ForeignKey, DateTime
from infra.base import Base

class InteracaoNPC(Base):
    __tablename__ = 'interacoes_npc'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    npc_id = Column(Integer, ForeignKey('npcs.id'), nullable=False)
    data = Column(DateTime, nullable=False)

    def __repr__(self):
        return (
            f"InteracaoNPC(id={self.id}, player_id={self.player_id}, "
            f"npc_id={self.npc_id}, data={self.data})"
        )