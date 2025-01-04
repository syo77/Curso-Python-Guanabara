"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

from os import system
system('cls')

lista_geral = []
lista_par = []
lista_impar = []
while True:
    while True:
        try:
            valor = int(input("Digite um número: "))
            lista_geral.append(valor)
            break
        except ValueError:
            print("ERRO. Digite um inteiro...")
    while True:
        finalizar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        if finalizar in 'sn':
            break
        else:
            print("Digite uma opção válida...")
    if finalizar == 'n':
        break
print("*****"*15)
lista_geral.sort()
print(f"A lista geral é: {lista_geral}, e contém '{len(lista_geral)}' elementos")
for numero in lista_geral:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
lista_par.sort()
lista_impar.sort()
print(f"A lista dos pares é: {lista_par}, e contém '{len(lista_par)}' elementos")
print(f"A lista dos ímpares é: {lista_impar}, e contém '{len(lista_impar)}' elementos")
