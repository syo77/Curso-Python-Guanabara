"""
Crie um programa em Python que:

1. Peça para o usuário inserir uma lista de números separados por espaço.
2. Converta essa entrada em uma lista de inteiros.
3. Remova os números duplicados e ordene a lista em ordem crescente.
4. Exiba a lista resultante.

Bônus:

Faça com que o programa funcione mesmo que o usuário insira espaços extras entre os números.
Implemente uma versão que utilize compreensão de listas.
"""

from os import system
system('cls')

def lista_numeros(lista):
    lista_formatada = []
    numeros_separados = lista.split()
    for numero in numeros_separados:
        try:
            num = int(numero)
            if num not in lista_formatada:
                lista_formatada.append(num)
        except ValueError:
            pass
    lista_formatada.sort()
    print(lista_formatada)
lista = str(input("Digite uma lista de números separados por espaço: "))
lista_numeros(lista)
print()
