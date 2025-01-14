"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada.
"""

from time import sleep
from os import system
system('cls')

print(">>>>>>> CONTAGEM DOS NÚMEROS <<<<<<<")
def contador(inicio, fim, passo):
    print(">>>>>>>", "-------", "<<<<<<<")
    print(f"CONTAGEM {inicio} A {fim}, {passo} EM {passo}")
    if passo == 0:
        passo += 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        for contar in range(inicio, fim+1, passo):
            print(contar, end=' → ', flush=True)
            sleep(0.3)
        print("/FIM/")
        print()
    else:
        for contar in range(inicio, fim-1, -passo):
            print(contar, end=' → ', flush=True)
            sleep(0.3)
        print("/FIM/")
        print()
contador(1, 10, 1)
contador(10, 0, 2)
print("CONTAGEM PERSONALIZADA: ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)

print()
