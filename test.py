from datetime import date
from models import Player, Fase, NPC, InteracaoNPC, Progresso, Tentativa, Conquista, PlayerConquista

# Criar um player
mia = Player(1, "Mia", 1200)
print(mia)

# Criar uma fase
fase1 = Fase(1, "O Pergaminho de Saturno", 1)
print(fase1)

# Criar um NPC
npc1 = NPC(1, "Guardião da Biblioteca", "Fornece pistas", "Coliseu")
print(npc1)

# Criar uma interação
interacao = InteracaoNPC(1, mia.id, npc1.id, date.today())
print(interacao)

# Criar progresso
progresso = Progresso(1, mia.id, fase1.id, date.today(), True, True, "Escolheu ajudar o NPC")
print(progresso)

# Criar tentativa
tentativa = Tentativa(1, mia.id, fase1.id, 3, 87.5, "solo", 900)
print(tentativa)

# Criar conquista
conquista = Conquista(1, "Descobriu o mural de Lyra")
print(conquista)

# Associar jogador à conquista
pc = PlayerConquista(mia.id, conquista.id, date.today())
print(pc)
