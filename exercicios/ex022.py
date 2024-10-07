"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome"""

nome = input("Digite seu nome completo: ").strip()
maiusculo = nome.upper()
minusculo = nome.lower()
divisao = nome.title().split()
letras_total = "".join(divisao)
print("Analisando seu nome...")
print(f"Seu nome maiúsculo é: {maiusculo}")
print(f"Seu nome minúsculo é: {minusculo}")
print(f"""Nome sem espaços: {letras_total}, quantidade: {len(letras_total)} letras""")
print(f"O primeiro nome que é {divisao[0]} tem: {len(divisao[0])} letras")

# Quantidade de letras sem contar os espaços: len(nome) - nome.count(" ") -> Quantidade total de letras - quantidade de espaços
# Quantidade de letras do primeiro nome: nome.find(" ") -> Conta qual a posição do primeiro espaço. (No python ele conta a posição - 1.)