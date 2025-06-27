from sqlalchemy import Column, Integer, DateTime, ForeignKey, PrimaryKeyConstraint
from infra.base import Base

class PlayerConquista(Base):
    __tablename__ = 'player_conquistas'

    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    conquista_id = Column(Integer, ForeignKey('conquistas.id'), nullable=False)
    data_desbloqueio = Column(DateTime, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('player_id', 'conquista_id'),
    )

    def __repr__(self):
        return (
            f"PlayerConquista(player_id={self.player_id}, conquista_id={self.conquista_id}, "
            f"data_desbloqueio={self.data_desbloqueio})"
        )