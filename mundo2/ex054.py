from datetime import date
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas não atingiram a maioridade e quantas já são maiores.
"""
maior = 0
menor = 0
for i in range(0, 7):
    ano_nasc = int(input(f"Digite o ano que a {i+1}ª pessoa nasceu: "))
    idade = date.today().year - ano_nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"\n{maior} pessoa(s) atingiram a maioridade")
print(f"{menor} pessoa(s) NÃO atingiram a maioridade")
