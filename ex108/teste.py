import moeda as mod_moeda
from os import system
system('cls')

valor = float(input("Digite o preço: R$ "))
desconto = int(input("Digite o desconto (número inteiro): "))

print("FORMATANDO O VALOR PELA FUNÇÃO MOEDA")
print()

print(f"Aumentando {desconto}% de {mod_moeda.formatar_moeda(valor)} temos {mod_moeda.formatar_moeda(mod_moeda.aumentar(valor, desconto))}")
print()

print(f"Diminuindo {desconto}% de {mod_moeda.formatar_moeda(valor)} temos {mod_moeda.formatar_moeda(mod_moeda.diminuir(valor, desconto))}")
print()

print(f"O dobro de {mod_moeda.formatar_moeda(valor)} é {mod_moeda.formatar_moeda(mod_moeda.dobro(valor))}")
print()

print(f"A metade de {mod_moeda.formatar_moeda(valor, '$')} é {mod_moeda.formatar_moeda(mod_moeda.metade(valor))}")
print()
