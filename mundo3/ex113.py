"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

from os import system
system('cls')

def leiaInt(frase):
    while True:
        try:
            numeroInt = int(input(frase))
            if numeroInt: # poderia remover esse if
                return numeroInt
        except (ValueError, TypeError):
            print("\033[31mINVÁLIDO. Digite apenas números inteiros...\033[m")
        except KeyboardInterrupt:
            print("\033[31mO usuário não quis inserir dados...\033[m")
            return "{vazio}"
        # else:
        #     return numeroInt

def leiaFloat(frase):
    while True:
        try:
            numeroFloat = float(input(frase))
            if numeroFloat: # poderia remover esse if
                return f"{numeroFloat}".replace('.',',')
        except (ValueError, TypeError):
            print("\033[31mINVÁLIDO. Digite apenas números reais...\033[m")
        except KeyboardInterrupt:
            print("\033[31mO usuário não quis inserir dados...\033[m")
            return "{vazio}"
        # else:
        #     return f"{numeroFloat}".replace('.',',')

numInt = leiaInt("Digite um número inteiro: ")
numFloat = leiaFloat("Digite um número real: ")
print(f"\033[32mO valor inteiro retornado foi \033[m{numInt} \033[32me o valor real foi \033[m{numFloat}\033[32m → FIM\033[m")
print()
