"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from os import system
system('cls')

from random import randint
lista = []
contador = 0
while True:
  numeros = randint(0, 10)
  lista.append(numeros)
  contador += 1
  if contador == 5:
    break
print("==="*15)
print(f"{'Gerador de 5 números aleatórios':^45}")
print("==="*15)
tupla = tuple(lista)
print(f"Os números gerados foram: {tupla}")

maior = 0
menor = 0
for posicao, numero in enumerate(tupla, start=0):
  if posicao == 0:
    maior = menor = numero
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
print(f"O maior valor foi: {maior}")
print(f"O menor valor foi: {menor}")
# print(f"O maior valor foi: {max(tupla)}")
# print(f"O menor valor foi: {min(tupla)}")
