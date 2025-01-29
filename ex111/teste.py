import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utilidadesYuri import moeda
from os import system
system('cls')

formatador = False
valor = float(input("Digite o preço: R$ "))
desconto1 = int(input("Digite o aumento (número inteiro): "))
desconto2 = int(input("Digite o desconto (número inteiro): "))

print()
print("%%%%%%%%% MOSTRANDO O RESUMO %%%%%%%%%")

moeda.resumo(valor, desconto1, desconto2)
print()
