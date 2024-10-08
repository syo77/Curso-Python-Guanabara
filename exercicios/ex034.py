"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00 , calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input("Escreva seu salário aqui: "))
if salario > 1250.00:
    aumento = salario * (1 + 10/100)
    print(f"O aumento do seu salário será de 10%, portanto você receberá {aumento}")
else:
    aumento = salario * (1 + 15/100)
    print(f"O aumento do seu salário será de 15%, portanto você receberá {aumento}")










