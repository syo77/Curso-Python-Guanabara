"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep
from os import system
system('cls')

print("---"*15)
print(f'{">>>>> PALPITES DA MEGA SENA <<<<<":^45}')
print("---"*15)

jogos = []
temporario = []
while True:
    try:
        quantidade_jogos = int(input("Digite a quantidade de jogos: "))
        if quantidade_jogos > 0:
            break
        else:
            print("INVÁLIDO. Digite um número maior que zero...")
    except ValueError:
        print("ERRO. DIGITE UM NÚMERO...")
print("Calculando...")
sleep(0.7)
if quantidade_jogos == 1:
    print(f">>>>>  IMPRIMINDO {quantidade_jogos} JOGO  <<<<<")
else:
    print(f">>>>>  IMPRIMINDO OS {quantidade_jogos} JOGOS  <<<<<")
while True:
    for quantidade in range(quantidade_jogos):
        for numero in range(0, 6):
            while len(temporario) < 6:
                numero = randint(1, 60)
                if numero not in temporario:
                    temporario.append(numero)
        temporario.sort()
        jogos.append(temporario[:])
        temporario.clear()
    for posicao, cada_jogo in enumerate(jogos):
        print(f"Jogo {posicao+1}: {jogos[posicao]}")
        sleep(0.5)
    break
print()
