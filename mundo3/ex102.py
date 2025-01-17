"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
from time import sleep
from os import system
system('cls')

def fatorial(numero=1, show=False):
    """
    :parâm numero: O número a ser calculado.
    :parâm show: (opcional) Se não for passado, imprime apenas o número. Se for, imprime a conta do fatorial.
    :return: O valor do fatorial do número passado.
    """
    fatorial_num = 1
    for contador in range(numero, 0, -1):
        if show == True:
            print(contador, end='')
            if numero == 1:
                print(' x 1', end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial_num *= contador
    return fatorial_num
print(">>>>>>> CALCULADORA DE FATORIAL <<<<<<<")
while True:
    ajuda = str(input("Deseja mostrar ajuda? [S/N]: ")).lower().strip()[0]
    if ajuda in 'sn':
        break
    print("INVÁLIDO. Digite S ou N...")
if ajuda == 's':
    print(">>>>>>> MOSTRANDO AJUDA <<<<<<<")
    sleep(0.5)
    help(fatorial)
while True:
    try:
        numero = int(input("Digite o número para obter seu fatorial: "))
        if numero > 0:
            break
        print("INVÁLIDO. Digite um número maior que zero...")
    except ValueError:
        print("ERRO. Digite apenas números...")
while True:
    contagem = str(input("Deseja mostrar a contagem? [S/N]: ")).lower().strip()[0]
    if contagem in 'sn':
        break
    print("INVÁLIDO. Digite S ou N...")
print(">>>>>>> OBTENDO RESULTADOS <<<<<<<")
sleep(0.5)
if contagem == 's':
    show = True
    print(f"A contagem do fatorial de {numero} é: ", end='')
    print(fatorial(numero, show))
else:
    print(f"O fatorial de {numero} é: {fatorial(numero)}")
print()
