"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "DEUS" """
cidade = input("Digite o nome da cidade: ").strip()
maiusculo = cidade.upper()
dividir = maiusculo.split()
começo = dividir[0]
print(f"O nome da cidade começa com 'Deus'? -> {"DEUS" in começo}")

#print(cidade[:5].upper() == 'DEUS')
#:5 lê do começo da string até o caractere 4 pq o 5 não se lê
#joga pra maiúsculo e verifica se é igual a 'DEUS'