"""
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é {maior:.1f}Kg")
print(f"O menor peso é {menor:.1f}Kg")
