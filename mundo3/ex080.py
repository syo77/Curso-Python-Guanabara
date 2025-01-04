"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

from os import system
system('cls')

lista = []
contador = 0
while contador < 5:
    while True:
        try:
            valor = int(input("Digite um valor: "))
            break
        except ValueError:
            print("ERRO. Insira um número inteiro!")
    if contador == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f"O valor '{valor}' foi adicionado ao final da lista...")
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f"O valor '{valor}' foi adicionado na posição ({posicao})...")
                break
            posicao += 1
    contador += 1
print("-=-"*20)
print(f"Os números digitados foram: {lista}\n")
