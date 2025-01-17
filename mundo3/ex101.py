"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto PROIBIDO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

from datetime import date
from os import system
system('cls')

def voto(ano_nascimento):
    # from datetime import date (só para lembrar que pode importar bibliotecas dentro da função)
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    """
    :parâm. ano_nascimento: Digite o ano do seu nascimento
    :return: calcula a idade da pessoa e retorna um valor literal 'PROIBIDO, OPCIONAL ou OBRIGATÓRIO' sobre voto
    """
    if idade < 16:
        status = 'PROIBIDO'
    elif idade >= 70 or idade <= 17:
        status = 'OPCIONAL'
    else:
        status = 'OBRIGATÓRIO'
    return f"É {status} votar com {idade} anos"
print(">>>>>>> Verificador de voto <<<<<<<")
while True:
    try:
        ano_nascimento = int(input("Digite o ano do seu nascimento: "))
        if ano_nascimento < 0 or ano_nascimento > date.today().year:
            print("INVÁLIDO. Digite o ano corretamente...")
        else:
            break
    except ValueError:
        print("ERRO. Digite apenas números...")
print(f"Status do voto: {voto(ano_nascimento)}")
print()
