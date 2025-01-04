"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

from os import system
system('cls')
lista = []
while True:
    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("ERRO. Insira um número inteiro!")
    while True:
        if valor not in lista:
            lista.append(valor)
            print("Valor adicionado...")
            break
        else:
            print("Número já inserido. Tente novamente...")
            break
    while True:
        finalizar = str(input("Deseja continuar? [S/N]: ")).strip().lower()[0]
        if finalizar in 'sn':
            break
        else:
            print("Resposta inválida. Digite [S/N]!")
    if finalizar == 'n':
        break
lista.sort()
print("==="*10)
print(f"Os valores digitados foram: {lista}\n")
