"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

import sys
import os
from time import sleep
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex115.biblioteca.menu import *

while True:
    resposta_usuario = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Finalizar Sistema'])
    if resposta_usuario == 1:
        cabecalho_menu('Opção1')
    elif resposta_usuario == 2:
        cabecalho_menu('Opção2')
    elif resposta_usuario == 3:
        print()
        cabecalho_menu('Encerrando programa... FIM!')
        break
    else:
        print("\033[31mERRO. Digite uma opção válida!\033[m")
    sleep(2)