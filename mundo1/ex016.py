"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""
from math import trunc
valor = float(input("Digite um número real: "))
print(f"\nO valor digitado foi {valor} e a sua parte inteira é {trunc(valor)}")
print("Ou")
print("Usando a conversão int()")
print(f"O valor digitado foi {valor} e a sua parte inteira é {int(valor)}")