"""
Faça um programa que receba um número e calcule um desconto de 5% no valor do produto.
"""
preco = float(input("Dê o preço do produto: "))
desconto = preco*(1-5/100)
print(f"O valor do produto é: {preco:.2f}")
print(f"Com desconto de 5% fica: {desconto:.2f}")