import moeda
from os import system
system('cls')

valor = float(input("Digite o preço: R$ "))
valor_formatado = f"{valor:.2f}"
desconto = int(input("Digite o desconto (número inteiro): "))

print(f"Aumentando {desconto}% de R${valor_formatado} temos R${moeda.aumentar(valor, desconto):.2f}")
print()

print(f"Diminuindo {desconto}% de R${valor_formatado} temos R${moeda.diminuir(valor, desconto):.2f}")
print()

print(f"O dobro de R${valor_formatado} é R${moeda.dobro(valor)::.2f}")
print()

print(f"A metade de R${valor_formatado} é R${moeda.metade(valor):.2f}")
print()
