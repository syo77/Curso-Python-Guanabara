"""
Faça um programa que leia um número qualquer e mostre seu fatorial
"""
numero = int(input("Digite o número desejado: "))
contador = numero
fatorial = 1
sequencia = ""
while contador > 1:
    fatorial *= contador
    sequencia += f"{contador} * "
    contador -= 1
sequencia += "1"
print(f"{numero}! = {sequencia} = {fatorial}")

# from math import factorial
# n = int(input("Digite um npumero para calcular seu fatorial: "))
# f = factorial(n)
# print(f"O fatorial de {n} é {f}")

# Código Guanabara
# n = int(input("Digite um número para calcular seu fatorial: "))
# c = n
# f = 1
# print(f"Calculando {n}! = ", end="")
# while c > 0:
#     print(f"{c}", end="")
#     print(" x " if c > 1 else " = ", end="")
#     f *= c
#     c -= 1
# print(f"{f}")