from datetime import date

class Player:
    def __init__(self, id, nome, pontuacao):
        self.id = id
        self.nome = nome
        self.pontuacao = pontuacao

class Fase:
    def __init__(self, id, titulo, ordem):
        self.id = id
        self.titulo = titulo
        self.ordem = ordem

class NPC:
    def __init__(self, id, nome, funcao, localizacao):
        self.id = id
        self.nome = nome
        self.funcao = funcao
        self.localizacao = localizacao

class InteracaoNPC:
    def __init__(self, id, player_id, npc_id, data):
        self.id = id
        self.player_id = player_id
        self.npc_id = npc_id
        self.data = data  # tipo date

class Progresso:
    def __init__(self, id, player_id, fase_id, data, missoes_cumpridas, puzzles_resolvidos, escolhas_narrativas=None):
        self.id = id
        self.player_id = player_id
        self.fase_id = fase_id
        self.data = data
        self.missoes_cumpridas = missoes_cumpridas
        self.puzzles_resolvidos = puzzles_resolvidos
        self.escolhas_narrativas = escolhas_narrativas

class Tentativa:
    def __init__(self, id, player_id, fase_id, numero_tentativas, tempo_resolucao, modalidade, pontuacao_obtida):
        self.id = id
        self.player_id = player_id
        self.fase_id = fase_id
        self.numero_tentativas = numero_tentativas
        self.tempo_resolucao = tempo_resolucao  # em segundos
        self.modalidade = modalidade  # "solo" ou "coop"
        self.pontuacao_obtida = pontuacao_obtida

class Conquista:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

class PlayerConquista:
    def __init__(self, player_id, conquista_id, data_desbloqueio):
        self.player_id = player_id
        self.conquista_id = conquista_id
        self.data_desbloqueio = data_desbloqueio

# atribuição de valor pras "variaveis"
player = Player(1, "Mia", 100)
fase = Fase(1, "O Pergaminho de Saturno", 1)

print(player)

print(fase)