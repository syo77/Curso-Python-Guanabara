"""
Crie um programa que leia e imprima o nome, ano de nascimento (idade) e a carteira de trabalho de uma pessoa, e cadastre-os (com idade) em um dicionário. Se por acaso a CPTS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
from time import sleep
from os import system
system('cls')

ano_atual = date.today().year
dados = {}

print(">>>>>>> PROGRAMA DO CLT <<<<<<<")
dados['NOME'] = str(input("Nome: ")).title().strip()
print('Cadastrado...')
while True:
    try:
        nascimento = int(input("Ano de nascimento: "))
        if nascimento >= 1919:
            print('Cadastrado...')
            break
        else:
            print("INVÁLIDO. Digite um ano verdadeiro...")
    except ValueError:
        print("ERRO. Digite o ano de seu nascimento...")
while True:
    if nascimento <= ano_atual:
        dados['IDADE'] = ano_atual - nascimento
        break
    else:
        print("ERRO. Você não veio do futuro...")
while True:
    try:
        dados['CTPS'] = int(input("Carteira de trabalho (0 = inexistente): "))
        if dados['CTPS'] >= 0:
            print('Cadastrado...')
            break
        else:
            print("INVÁLIDO. Digite um número de CTPS válido...")
    except ValueError:
        print("ERRO. Insira apenas números...")
if dados['CTPS'] != 0:
    while True:
        try:
            dados['CONTRATAÇÃO'] = int(input("Ano de Contratação: "))
            if dados['CONTRATAÇÃO'] >= 1919:
                print('Cadastrado...')
                break
            else:
                print("INVÁLIDO. Digite um ano real....")
        except ValueError:
            print("ERRO. Digite apenas números...")
    tempo_contribuição = ano_atual - dados['CONTRATAÇÃO']
    meta_contribuição = 35
    dados['APOSENTADORIA'] = (meta_contribuição - tempo_contribuição) + dados['IDADE']
    while True:
        try:
            dados['SALÁRIO'] = float(input("Salário: R$ "))
            if dados['SALÁRIO'] > 0:
                print('Cadastrado...')
                break
            else:
                print("INVÁLIDO. Digite seu salário corretamente...")
        except ValueError:
            print("ERRO. Insira apenas números...")
print("-------"*12)
print(">>>>>>> GERANDO RESULTADOS <<<<<<<")
sleep(1.2)
for chave, valor in dados.items():
    print(f"{chave} tem o valor {valor}")
    sleep(0.5)
print()
