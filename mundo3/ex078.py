"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

from os import system
system('cls')
lista = []
maior = 0
menor = 0
contador = 0
while contador < 5:
    while True:
        try:
            valor = int(input(f"Digite um número na posição {contador}: "))
            break
        except ValueError:
            print("Erro. Digite um número válido")
    lista.append(valor)
    if contador == 0:
        maior = menor = valor
    else:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor
    contador += 1
print(f"Os números digitados foram: {lista}")
print(f"O maior valor foi {maior} nas posições: ", end='')
for indice, numero in enumerate(lista):
    if numero == maior:
        print(f"({indice})", end=' ')
print(f"\nO menor valor foi {menor} nas posições: ", end='')
for indice, numero in enumerate(lista):
    if numero == menor:
        print(f"({indice})", end=' ')
print('\n')
