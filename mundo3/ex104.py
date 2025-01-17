"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um número: ')
"""

from sys import stdin
from os import system
system('cls')

def meu_input(entrada_usuario=''):
    print(entrada_usuario, end='', flush=True)
    mensagem_input = stdin.readline().strip()
    return mensagem_input

def leiaInt(suposto_numero):
    verificador = False
    valor = 0
    while True:
        numero = str(meu_input(suposto_numero))
        if numero.isnumeric():
            valor = int(numero)
            verificador = True
        else:
            print("\033[0;31mERRO. Digite um número corretamente...\033[m")
        if verificador == True:
            break
    return valor
print()
print("\033[0;36m>>>>>>> VERIFICADOR DE NÚMEROS <<<<<<<\033[m")
numero = leiaInt('Digite um número: ')
print(f"\033[0;32mVocê digitou o número: {numero}\033[m")
print("\033[0;32m... FIM DO PROGRAMA ...\033[m")
print("\033[0;46m--\033[m"*19)
print()
