"""
Faça um mini-sistema que utilize o interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
"""

from os import system
system('cls')

cores = {'sem cor':'\033[0m', 'vermelho':'\033[0;30;41m', 'azul claro':'\033[0;30;46m', 'verde claro':'\033[0;30;42m', 'branco':'\033[7;30m'}

def mostrar_sistema(comando):
    titulo(f"Imprimindo o manual do comando '{comando}'", 'azul claro')
    print(cores['branco'])
    help(comando)
    print(cores['sem cor'])

def titulo(mensagem, cor=''):
    tam = len(mensagem) + 4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {mensagem}  ')
    print('~'*tam)
    print(cores['sem cor'])

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYTHON', 'verde claro')
    comando = str(input("Digite uma Função ou Biblioteca: ")).lower()
    if comando == 'fim':
        break
    else:
        mostrar_sistema(comando)
titulo('ATÉ LOGO', 'vermelho')
print()
