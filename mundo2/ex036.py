"""
Escreva um programa em Python para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

print("--=--"*20)
print("Cálculo de aprovação de empréstimo")
print("--=--"*20)

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário mensal: "))
tempo = int(input("Digite em quantos meses irá pagar a dívida: "))

valor_prestacao = valor_casa / tempo
if valor_prestacao > salario * (30/100):
    print("""\nO empréstimo foi negado!
O valor excede 30% do salário.""")
    print(f"Seu salário é de R${salario:.2f} e o valor de cada prestação é de {valor_prestacao:.2f}")
elif valor_prestacao == salario * (30/100):
    print("\nSeu salário é igual a prestação mensal, FOI APROVADO mas você vai ficar pobre!")
    print(f"Seu salário é de R${salario:.2f} e o valor de cada prestação é de {valor_prestacao:.2f}")
else:
    print("\nEmprétimo aprovado!")
    print(f"Seu salário é de R${salario:.2f} e o valor de cada prestação é de {valor_prestacao:.2f}")
print("---> FIM <---")
