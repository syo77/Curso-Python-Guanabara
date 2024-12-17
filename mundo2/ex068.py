"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
"""
from random import randint
jogador = 0
resultado = 0
vitorias = 0
print("---"*10)
print("JOGO DO PAR OU ÍMPAR")
print("---"*10)
while True:
    while True:
        parouimpar = str(input("Par ou Ímpar? (P/I): ")).strip()[0]
        if parouimpar.lower() in 'pi':
            break
        else:
            print("Inválido. Tente novamente!")
    computador = randint(0, 10)
    while True:
        jogador = int(input("Digite um número: "))
        if jogador > 10 or jogador < 0:
            print("Inválido. Digite um número de (0 a 10). Afinal, você só tem 10 dedos nas mãos: ")
        else:
            break
    resultado = jogador + computador
    if parouimpar.lower() == 'p':
        if resultado % 2 == 0:
            vitorias += 1
            print("-=-"*10)
            print("VOCÊ GANHOU!")
            print(f"O computador jogou {computador}")
        else:
            break
    if parouimpar.lower() == 'i':
        if resultado % 2 != 0:
            vitorias += 1
            print("-=-"*10)
            print("VOCÊ GANHOU!")
            print(f"O computador jogou {computador}")
        else:
            break
print("-=-"*10)
print("VOCÊ PERDEU!")
print(f"Computador jogou {computador}")
if resultado % 2 == 0:
    print(f"O total foi {resultado} que é par")
else:
    print(f"O total foi {resultado} que é ímpar")
print(f"Total de vitórias: {vitorias}")
