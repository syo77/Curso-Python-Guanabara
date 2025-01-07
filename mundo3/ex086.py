"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

from os import system
from time import sleep
system('cls')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite o valor para [{linha}, {coluna}]: "))
print("---"*15)
print("Imprimindo a matriz...")
sleep(1)
for printar_linha in range(0, 3):
    for printar_coluna in range(0, 3):
        print(f"[{matriz[printar_linha][printar_coluna]:^5}]", end=' ')
    print()
