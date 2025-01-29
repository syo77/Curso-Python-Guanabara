import moeda as mod_moeda
from os import system
system('cls')

formatador = False
valor = float(input("Digite o preço: R$ "))
desconto = int(input("Digite o desconto (número inteiro): "))
formatar = str(input("Deseja formatar o valor? [S/N]: ")).lower().strip()[0]
while formatar not in 'sn':
    formatar = str(input("Entrada inválida. Deseja formatar o valor? [S/N]: ")).lower().strip()[0]
if formatar == 's':
    formatador = True

print()
print("FORMATANDO OPCIONALMENTE O VALOR PELA FUNÇÃO MOEDA")
print()

print(f"Aumentando {desconto}% de {mod_moeda.formatar_moeda(valor, formatar=formatador)} temos {mod_moeda.formatar_moeda(mod_moeda.aumentar(valor, desconto), formatar=formatador)}")
print()

print(f"Diminuindo {desconto}% de {mod_moeda.formatar_moeda(valor, formatar=formatador)} temos {mod_moeda.formatar_moeda(mod_moeda.diminuir(valor, desconto), formatar=formatador)}")
print()

print(f"O dobro de {mod_moeda.formatar_moeda(valor, formatar=formatador)} é {mod_moeda.formatar_moeda(mod_moeda.dobro(valor), formatar=formatador)}")
print()

print(f"A metade de {mod_moeda.formatar_moeda(valor, '$', formatar=formatador)} é {mod_moeda.formatar_moeda(mod_moeda.metade(valor),formatar=formatador)}")
print()
