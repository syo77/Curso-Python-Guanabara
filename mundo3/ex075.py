"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
from os import system
system('cls')

lista = []
for n in range(0,4):
    while True:
        try:
            numero = int(input("Digite um número: "))
            break
        except ValueError:
            print("Tente novamente. Digite um número válido")
    lista.append(numero)
tupla = tuple(lista)
print("\nOs números digitados foram: ", end='')
for i, n in enumerate(tupla):
    if i == len(tupla)-1:
        print(n)
    else:
        print(n, end=', ')
print(f"O número 9 apareceu {tupla.count(9)} vezes")
try:
    print(f"O número 3 apareceu no {tupla.index(3)}º *índice* ")
except ValueError:
    print("O número 3 não apareceu na tupla")
# if 3 in tupla:
#     print(f"O número 3 apareceu no {tupla.index(3)}º *índice* ")
# else:
#     print("O número 3 não apareceu na tupla")
print("Os números pares são: ",end='')
primeiro_par = True
for par in tupla:
    if par % 2 == 0:
        if primeiro_par:
            print(par, end='')
            primeiro_par = False
        else:
            print(f", {par}", end='')
print('\n')
