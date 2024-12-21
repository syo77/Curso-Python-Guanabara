"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

from os import system
system('cls')

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    try:
        selecao = int(input("Digite um número de 0 a 20: "))
        if selecao < 0 or selecao > 20:
            print("Erro. Tente novamente!")
        else:
            break
    except ValueError:
            print("Inválido. Insira um número válido!")
print(f"Você selecionou o número {contagem[selecao]}")

"""
Se caso o usuário desejar continuar
"""

while True:
    try:
        print("--=--"*10)
        selecao = int(input("Digite um número de 0 a 20: "))
        if 0 < selecao > 20:
            print("Erro. Tente novamente!")
    except ValueError:
        print("Inválido. Insira um número valido!")
    while True:
        finalizar = str(input("Deseja continuar? [S/N]: ")).strip().lower()[0]
        if finalizar in 'sn':
            break
        else:
            print("Tente novamente!")
    print(f"Você digitou o número {contagem[selecao]}")
    print("--=--"*10)
    if finalizar == 'n':
        break
    