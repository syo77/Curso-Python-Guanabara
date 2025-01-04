"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado ou não está na lista.
"""

from os import system
system('cls')

lista = []
while True:
    while True:
        try:
            valor = int(input("Digite um número: "))
            lista.append(valor)
            break
        except ValueError:
            print("ERRO. DIGITE UM NÚMERO INTEIRO!")
    while True:
        finalizar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        if finalizar in 'sn':
            break
        else:
            print("Digite a opção correta S ou N...")
    if finalizar == 'n':
        break
lista.sort(reverse=True)
print("*****"*15)
print(f"Foram digitados '{len(lista)}' números")
print(f"A lista em ordem descrescente: {lista}")
if 5 in lista:
    print("O valor 5 foi encontrado na lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
print("\n")
