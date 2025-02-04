"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

import sys
import os
from time import sleep
from os import system
system('cls')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex115.biblioteca.menu import *
from ex115.biblioteca.arquivo import *

nome_arquivo = "biblia.txt"
nome_arquivo2 = "exortacao.txt"

if not validar_arquivo(nome_arquivo):
    criarArquivo(nome_arquivo)

while True:
    resposta_usuario = menu(['Listar Palavras', 'Cadastrar Palavra', 'Remover última linha', 'Finalizar Sistema'])
    if resposta_usuario == 1:
        lerArquivo(nome_arquivo)
    elif resposta_usuario == 2:
        cabecalho_menu("NOVO CADASTRO")
        nome_livro = str(input("Digite o nome do livro: ")).title().strip()
        try:
            capitulo_livro = int(input("Digite o capitulo do livro: "))
        except (ValueError, TypeError):
            capitulo_livro = 1
        try:
            verso_capitulo = int(input("Digite o verso do capitulo: "))
        except (ValueError, TypeError):
            verso_capitulo = 1
        cadastrar(nome_arquivo, nome_livro, capitulo_livro)
    elif resposta_usuario == 3:
        remover_ultima_linha(nome_arquivo)
    elif resposta_usuario == 4:
        print()
        cabecalho_menu("Encerrando programa... FIM!")
        break
    else:
        print("\033[31mERRO. Digite uma opção válida!\033[m")
    sleep(1)
print()
