from sqlalchemy import Column, Integer, Float, String, ForeignKey
from infra.base import Base

class Tentativa(Base):
    __tablename__ = 'tentativas'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    fase_id = Column(Integer, ForeignKey('fases.id'), nullable=False)
    numero_tentativas = Column(Integer, nullable=False)
    tempo_resolucao = Column(Float, nullable=False)  # Tempo em segundos, por exemplo
    modalidade = Column(String(50), nullable=False)
    pontuacao_obtida = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"Tentativa(id={self.id}, player_id={self.player_id}, fase_id={self.fase_id}, "
                f"tentativas={self.numero_tentativas}, tempo={self.tempo_resolucao}, "
                f"modalidade='{self.modalidade}', pontuacao={self.pontuacao_obtida})")

    def to_dict(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "fase_id": self.fase_id,
            "numero_tentativas": self.numero_tentativas,
            "tempo_resolucao": self.tempo_resolucao,
            "modalidade": self.modalidade,
            "pontuacao_obtida": self.pontuacao_obtida
        }