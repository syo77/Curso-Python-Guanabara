"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, o dois são iguais
"""
maior = 0
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print(f"Entre os números {num1} e {num2} o maior valor é {num1}")
elif num2 > num1:
    print(f"Entre os números {num1} e {num2} o maior valor é {num2}")
else:
    print("Não existe maior valor, o dois números são iguais")