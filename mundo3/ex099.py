"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep
from os import system
system('cls')

def maior(*numeros):
    maior = 0
    for posicao, numero in enumerate(numeros):
        if posicao == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
    print(">>>>>>> Analisando todos os valores passados... <<<<<<<")
    sleep(0.7)
    print(f"Os números são: {numeros}")
    print(f"O maior número é: {maior}")
lista_numeros = []
while True:
        try:
            numeros = int(input("Digite um número (999 iterrompe): "))
        except ValueError:
            print("ERRO. Digite apenas números...")
        if numeros == 999:
            break
        lista_numeros.append(numeros)
maior(*lista_numeros)

print()
