"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

from os import system
system('cls')

expressao = str(input("Digite a expressão: "))
contador = 0
for char in expressao:
    if char == '(':
        contador += 1
    elif char == ')':
        contador -= 1
    if contador < 0:
        print("Expressão inválida!")
        break
else:
    if contador == 0:
        print("Expressão válida!")
    else:
        print("Expressão inválida!")
print("\n")