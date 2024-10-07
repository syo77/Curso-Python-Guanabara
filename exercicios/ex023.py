"""Faça um programa que leia um npumero de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade:4
dezena:3
centena:8
milhar:1"""

numero = int(input("Digite um número: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f"""O número é: {numero}
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}""")