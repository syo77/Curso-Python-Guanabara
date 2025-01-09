"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. (Mostre a situação do aluno)
"""

from os import system
system('cls')

dicionario = {}
dicionario['nome'] = str(input("Digite o nome do aluno: ")).title().strip()
while True:
    try:
        dicionario['média'] = float(input(f"Digite a média de {dicionario['nome']}: "))
        if dicionario['média'] < 0 or dicionario['média'] > 10:
            print("INVÁLIDO. Digite média corretamente...")
        else:
            break
    except ValueError:
        print("ERRO. Digite apenas números...")
if dicionario['média'] >= 7:
    dicionario['situação'] = 'Aprovado'
elif dicionario['média'] < 7 and dicionario['média'] >= 5:
    dicionario['situação'] = 'Recuperação'
else:
    dicionario['situação'] = 'Reprovado'
print(">>>"*7, "<<<"*7)
for chave, valor in dicionario.items():
    print(f">>> {chave} é igual a {valor}")
