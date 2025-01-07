"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

from os import system
system('cls')

# Primeiro código com lista composta

geral = [[], []]
for contador in range (0, 7):
    while True:
        try:
            numero = int(input(f"Digite o {contador+1}º número: "))
            break
        except ValueError:
            print("ERRO. Digite um NÚMERO")
    if numero % 2 == 0 and numero not in geral[0]:
        geral[0].append(numero)
    if numero % 2 != 0 and numero not in geral[1]:
        geral[1].append(numero)

geral[0].sort()
geral[1].sort()
print(f"Os números são: {geral}")
print(f"Os números pares são: {geral[0]}")
print(f"Os números ímpares são: {geral[1]}")

print('\n')

# Segundo código com uma lista só

geral = []
for contador in range(0, 7):
    numero = int(input(f"Digite o {contador+1}º número: "))
    geral.append(numero)
geral.sort()
print("Os números pares são: ", end='')
for num_par in geral:
    if num_par % 2 == 0:
        print(f"{num_par}", end=' → ')
print("Fim dos pares")
print("Os números ímpares são: ", end='')
for num_impar in geral:
    if num_impar % 2 != 0:
        print(f"{num_impar}", end=' → ')
print("Fim dos ímpares")

print('\n')
