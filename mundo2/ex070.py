"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
"""
preco = 0
total = 0
nomemaisbarato = ''
continuar = ''
maisbarato = 0
contador = 0
prodmaismil = 0
while True:
    nome = str(input("Produto: ")).strip().capitalize()
    while True:
        try:
            preco = float(input("Digite o preço: R$ "))
            if preco > 0:
                break
            else:
                print("Digite um número maior que zero. Tente novamente!")
        except ValueError:
            print("Inválido. Digite um número inteiro ou decimal")
    contador += 1
    total += preco
    if preco > 1000:
        prodmaismil += 1
    if contador == 1:
        maisbarato = preco
        nomemaisbarato = nome
    else:
        if preco < maisbarato:
            maisbarato = preco
            nomemaisbarato = nome
    # if contador == 1 or preco < maisbarato:
    #     maisbarato = preco
    #     nomemaisbarato = nome
    while True:
        try:
            continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
            if continuar in 'sn':
                break
            else:
                print("Inválido. Tente novamente")
        except ValueError:
            print("Inválido. Digite S ou N")
    if continuar == 'n':
        break
print(f"O valor total gasto foi R$ {total:.2f}")
print(f"Existem '{prodmaismil}' produtos que custam mais de mil reais")
print(f"O produto mais barato é {nomemaisbarato} e custa R$ {maisbarato:.2f}")
  