"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
contador = 0
numeros_digitados = []
for i in range(0, 6):
    numeros = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros_digitados.append(numeros)
    if numeros % 2 == 0:
        soma += numeros
        contador += 1
print(f"\nOs números digitados foram: {numeros_digitados}")
print(f"A quantidade de números pares é igual a {contador} e a soma deles é igual a {soma}")