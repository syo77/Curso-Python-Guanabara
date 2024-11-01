"""
Faça um programa que leia o nome completo de um pessoa, mostrando em seguida o primeiro nome e o último nome separadamente
Ex: Yuri Victor de Oliveira e Silva
Primeiro: Yuri
Último: Silva
"""
nome = input("Digite seu nome: ").strip() 
nome_low = nome.lower()
dividir = nome_low.title().split()
tamanho = len(dividir)
print(f"""O seu nome é: {nome.title()}
Primeiro nome: {dividir[0]}
Último nome: {dividir[-1]}""")
# Não pode usar dividir[tamanho (do split)] pq ele começa a contar a partir de 1 e não de 0, assim excedendo o tamanho máximo da lista
# Teria que usar dividir[tamanho-1] pra funcionar