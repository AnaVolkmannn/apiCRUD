from flask import Flask, jsonify, request
from models.player import Player
from models.npc import NPC
from models.fase import Fase
from models.interacao_npc import InteracaoNPC
from models.progresso import Progresso
from models.tentativa import Tentativa
from models.conquista import Conquista
from models.player_conquista import PlayerConquista

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
