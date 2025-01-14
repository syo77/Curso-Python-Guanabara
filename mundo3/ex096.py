"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a áres do terreno.
"""

from os import system
system('cls')

def area(largura, comprimento):
    area = largura*comprimento
    print(f"O seu terreno é de {largura:.2f} X {comprimento:.2f} metros, e tem uma área de {area:.2f}m²")
largura = float(input("Digite a largura (metros) do terreno: "))
comprimento = float(input("Digite o comprimento (metros) do terreno: "))
print(">>>>>>> RESULTADO <<<<<<<")
area(largura, comprimento)

print()