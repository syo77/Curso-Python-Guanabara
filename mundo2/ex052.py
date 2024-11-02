"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input("Digite um número inteiro: "))
total = 0
for i in range(1, num+1):
    if num % i == 0:
        print("\033[33m", end=" ")
        total +=1
    else:
        print("\033[31m", end=" ")
    print(f"{i}", end="")
print(f"\n\033[mO número {num} foi divisível {total} veze(s)")
if total == 2:
    print("O número É PRIMO")
else:
    print("O número NÃO É PRIMO")