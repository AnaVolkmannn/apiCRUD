from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from infra.base import Base

class Progresso(Base):
    __tablename__ = 'progresso'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    fase_id = Column(Integer, ForeignKey('fases.id'), nullable=False)
    data = Column(DateTime, nullable=False)
    missoes_cumpridas = Column(Integer, default=0)
    puzzles_resolvidos = Column(Integer, default=0)
    escolhas_narrativas = Column(Text, nullable=True)

    def __repr__(self):
        return (f"Progresso(id={self.id}, player_id={self.player_id}, fase_id={self.fase_id}, "
                f"data={self.data}, missoes_cumpridas={self.missoes_cumpridas}, "
                f"puzzles_resolvidos={self.puzzles_resolvidos}, escolhas='{self.escolhas_narrativas}')")

    def to_dict(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "fase_id": self.fase_id,
            "data": self.data.isoformat() if self.data else None,
            "missoes_cumpridas": self.missoes_cumpridas,
            "puzzles_resolvidos": self.puzzles_resolvidos,
            "escolhas_narrativas": self.escolhas_narrativas
        }