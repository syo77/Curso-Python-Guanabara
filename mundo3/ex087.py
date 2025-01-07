"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

--- DESAFIO ANTERIOR ---

(Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.)
"""

from os import system
from time import sleep
system('cls')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_3col = maior_2linha = 0
for linha in range(0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f"Digite o valor para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        if coluna == 2:
            soma_3col += matriz[linha][coluna]
        if linha == 1 and coluna == 0:
            maior_2linha = matriz[linha][coluna]
        elif linha == 1 and coluna > 0:
            if matriz[linha][coluna] > maior_2linha:
                maior_2linha = matriz[linha][coluna] 

print("%%%"*19)
print("Imprimindo a matriz...")
sleep(1)
for printar_linha in range(0, 3):
    for printar_coluna in range(0, 3):
        print(f"[{matriz[printar_linha][printar_coluna]:^5}]", end=' ')
    print()
print(f"A soma de todos os números pares é igual a: {soma_par}")
print(f"A soma da terceira coluna é igual a: {soma_3col}")
print(f"O maior valor da segunda linha é: {maior_2linha}")

print('\n')
