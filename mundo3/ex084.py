"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
from os import system
system('cls')

resultado = []
contador_pessoas = 1
maior = menor = 0
pessoa_maior_peso = []
pessoa_menor_peso = []
print("%%%%%"*10)
print(f"{'Analisador de peso':^50}")
print("%%%%%"*10)
while True:
    dados = []
    nome = str(input("Nome: ")).capitalize()
    dados.append(nome)
    peso = float(input("Peso: "))
    dados.append(peso)
    resultado.append(dados[:])

    if len(resultado) == 1:
        maior = menor = peso
        pessoa_maior_peso = [nome]
        pessoa_menor_peso = [nome]
    else:
        if peso > maior:
            maior = peso
            pessoa_maior_peso = [nome]
        elif peso == maior:
            pessoa_maior_peso.append(nome)
        if peso < menor:
            menor = peso
            pessoa_menor_peso = [nome]
        elif peso == menor:
            pessoa_menor_peso.append(nome)

    while True:
        finalizar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        if finalizar in 'sn':
            break
        else:
            print("INVÁLIDO. Digite uma opção correta...")
    if finalizar == 'n':
        break
print(f"A lista completa é: {resultado}")
print(f"Foram cadastradas '{len(resultado)}' pessoas")
print(f"O maior peso é {maior} e pertence a {', '.join(pessoa_maior_peso)}")
print(f"O menor peso é {menor} e pertence a {', '.join(pessoa_menor_peso)}")
