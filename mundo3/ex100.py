"""
Faça um programa que tenha uma lista chamada números duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
"""

from time import sleep
from random import randint
from os import system
system('cls')

numeros = []

print(">>>>>>> SORTEADOR E SOMADOR <<<<<<<")

def sorteia(lista_numeros):
    while len(lista_numeros) < 5:
        aleatorio = randint(1, 10)
        if aleatorio not in lista_numeros:
            lista_numeros.append(aleatorio)
sorteia(numeros)
print(">>> SORTEANDO <<<")
for contador in range(10, 0, -1):
    print("."*contador, f"{contador}")
    sleep(0.5)
    contador -= 1
print(">>>>>>> ------- <<<<<<<")
for posicao, valor in enumerate(numeros, start=1):
    sleep(0.5)
    print(f"{posicao}º Número: {valor}")
print(">>> ANALISANDO RESULTADOS <<<")
sleep(1)
print("Os números sorteados foram: ", end='')
for valor in numeros:
    print(valor, end=' ')
print()
def somaPar(*numeros_int):
    soma = 0
    for valor in numeros_int:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma dos números pares de {numeros} é igual a: {soma}")
somaPar(*numeros)

print()







# def sorteia():
#     contador = 1
#     while len(numeros) < 5:
#         aleatorio = randint(1, 10)
#         if aleatorio not in numeros:
#             print(f"{contador}º Número: {aleatorio}")
#             sleep(0.4)
#             contador += 1
#             numeros.append(aleatorio)
#     print(">>> ANALISANDO RESULTADOS <<<")
#     sleep(1)
#     print(f"Os números sorteados foram: ", end='')
#     for valor in numeros:
#         print(valor, end=' ')