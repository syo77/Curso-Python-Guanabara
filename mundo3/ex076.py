"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular.
"""
from os import system
system('cls')

materiais_escolares = ("Caderno", 15.90, "Lápis", 1.50, "Caneta", 2.50, "Borracha", 0.99, "Estojo", 12.30, "Mochila", 89.90, "Régua", 4.20, "Apontador", 3.75, "Marcador de Texto", 6.80, "Papel A4 (500 folhas)", 24.50)

lista = []
while True:
    produto = str(input("Digite o nome do produto: ")).capitalize().strip()
    if not produto:
        print("Nome inválido. Tente novamente!")
        continue
    while True:
        try:
            preco = float(input("Digite o preço: "))
            if preco < 0:
                print("Inválido. Insira um número maior que zero.")
            else:
                break
        except ValueError:
            print("Inválido. Tente novamente!")
    lista.append(produto)
    lista.append(preco)
    continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
    if continuar == 'n':
        break
tupla = tuple(lista)
print("-"*45)
print(f"{'LISTAGEM DE PRODUTOS':^45}")
print("-"*45)
for posicao, nome_do_produto in enumerate(materiais_escolares):
    if posicao % 2 == 0:
        pontinhos = int(30-len(nome_do_produto))
        print(f"{nome_do_produto}", end='')
        print("."*pontinhos, end='')
    else:
        print(f"R$ {nome_do_produto:>7.2f}")
