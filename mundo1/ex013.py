"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input("Insira o seu salário: R$"))
aumento = salario*(1+15/100)
print(f"Seu salário é de: R${salario:.2f}")
print(f"Seu salário com 15% de aumento é de: R${aumento:.2f}")