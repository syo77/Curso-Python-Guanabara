import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utilidadesYuri import moeda
from utilidadesYuri import dado
from os import system
system('cls')

formatador = False
valor = dado.leiaDinheiro("Digite o valor: ")
desconto1 = int(input("Digite o aumento (número inteiro): "))
desconto2 = int(input("Digite o desconto (número inteiro): "))

print()
print("%%%%%%%%% MOSTRANDO O RESUMO %%%%%%%%%")

moeda.resumo(valor, desconto1, desconto2)
print()
