jogadores_gols = {"Pelé": 767, "CR7": 850, "Messi": 825, "Rogério Ceni": 131}

mais_gols = 0
jogador_mais_gols = " "

for x, y in jogadores_gols.items():
    if y > mais_gols:
        mais_gols = y
        jogador_mais_gols = x

print(f"{jogador_mais_gols} é o jogador com mais gols, com {mais_gols} no total!")