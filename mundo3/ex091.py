"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
"""

from os import system
system('cls')
from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
ranking = {}
for contador_jogador in range(0, 4):
    jogo[f'jogador{contador_jogador+1}'] = randint(1,6)
print("Os resultados foram:")
for chave, valor in jogo.items():
    print(f"O {chave} tirou {valor} no dado")
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(">"*19, "<"*19)
print("   >< >< RANKING >< ><")
for posicao, elemento in enumerate(ranking, start=1):
    print(f"{posicao}º lugar >>> {elemento[0]} com {elemento[1]}")
