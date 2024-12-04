"""
Escreva um programa que leia um número inteiro "n" qualquer e mostre na tela os "n" primeiros elementos de uma Sequência de Fibonacci
"""
numero_elementos = int(input("Digite a quantidade de elementos da Sequência de Fibonacci: "))
contador = 3
elemento1 = 0
elemento2 = 1
print("~~~"*10)
print(f"Sequência: {elemento1} → {elemento2} → ", end='')
while contador <= numero_elementos:
    elemento3 = elemento1 + elemento2
    print(f"{elemento3}", end=' → ')
    elemento1 = elemento2
    elemento2 = elemento3
    contador += 1
print("FIM")
