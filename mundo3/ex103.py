"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
"""

from os import system
system('cls')

def ficha(nome='<indivíduo indigente>', gols=0):
    return f'O jogador {nome} marcou {gols} gol(s)'
print(">>>>>>> IMPRESSORA DE FICHA <<<<<<<")
nome = str(input("Digite o nome do jogador: ")).strip().title()
qtd_gols = str(input("Digite a quantidade de gols: "))
if not qtd_gols.isnumeric():
    qtd_gols = 0
if not nome:
    print(ficha(gols=qtd_gols))
else:
    print(ficha(nome, qtd_gols))
print()
