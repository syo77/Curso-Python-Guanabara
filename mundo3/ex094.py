"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""

from os import system
system('cls')

lista_pessoas = []
soma_idade = 0

while True:
    pessoas = {}
    pessoas['Nome'] = str(input("Nome: ")).title().strip()
    print("Cadastrado...")
    while True:
        pessoas['Sexo'] = str(input("Sexo: ")).upper().strip()[0]
        if pessoas['Sexo'] in 'MF':
            print("Cadastrado...")
            break
        print("INVÁLIDO. Digite M ou F...")
    while True:
        try:
            pessoas['Idade'] = int(input("Idade: "))
            if pessoas['Idade'] < 0:
                print("INVÁLIDO. Digite a idade corretamente...")
            else:
                print("Cadastrado...")
                soma_idade += pessoas['Idade']
                break
        except ValueError:
            print("ERRO. Digite apenas números...")
    lista_pessoas.append(pessoas.copy())
    while True:
        continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        if continuar in 'sn':
            break
        print("INVÁLIDO. Digite S ou N...")
    if continuar == 'n':
        print(">>> GERANDO RESULTADOS")
        break
    print("Continuando...")
media_idade = soma_idade / len(lista_pessoas)
print(">"*19, "<"*19)
print(lista_pessoas)
print(f"<<< Foram cadastradas {len(lista_pessoas)} pessoas")
print(f"<<< A média de idade é: {media_idade:.2f}")
print(f"<<< As mulheres cadastradas foram: ", end='')
lista_mulheres = []
for pessoa in lista_pessoas:
    for dados in pessoa.values():
        if dados == 'F':
            # print(pessoa['Nome'], end=' || ') isso já resolveria
            lista_mulheres.append(pessoa['Nome'])
print(lista_mulheres)
print("<<< A lista de pessoas com a idade maior que a média é: ")
for pessoa in lista_pessoas:
    if pessoa['Idade'] > media_idade:
        print(f"<<<<<<< {pessoa['Nome']} com idade de {pessoa['Idade']} anos")
print()
