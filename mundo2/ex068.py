"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
"""

from random import randint
computador = randint(0, 10)
jogador = 0
while True:
    while True:
        parouimpar = str(input("Par ou Ímpar? (P/I): ")).strip()[0]
        if parouimpar.lower() in 'pi':
            break
        else:
            print("Inválido. Tente novamente!")
    while True:
        jogador = int(input("Digite um número: "))
        if jogador > 10 or jogador < 0:
            print("Inválido. Digite um número de (0 a 10). Afinal, você só tem 10 dedos nas mãos: ")
        else:
            break
    resultado = jogador + computador
    par = resultado % 2 == 0
    impar = resultado % 2 != 0
    # if resultado == par:
    # if parouimpar.lower() == 
    if jogador != computador:
        break

