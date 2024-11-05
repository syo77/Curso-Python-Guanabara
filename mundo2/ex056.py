"""
Desenvolva um programa em Python que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos.
"""
M_menos20 = 0
H_maior_idade = 0
soma_idade = 0
nome_H_mais_velho = []
nome_mulheres = []
for i in range(1,5):
    print(f"---- {i}ª PESSOA ----")
    nome = input("Nome: ").strip().title()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    soma_idade += idade
    if sexo == 'M':
        if idade > H_maior_idade:
            H_maior_idade = idade
            nome_H_mais_velho = [nome]
        elif idade == H_maior_idade:
            nome_H_mais_velho.append(nome)
    if sexo == 'F':
        nome_mulheres.append(nome)
        if idade < 20:
            M_menos20 += 1
media_idade = soma_idade / 4
print(f"A quantidade de mulheres menor de 20 anos é: {M_menos20}")
print(f"O nome das mulheres digitadas é: {', '.join(nome_mulheres)}")
print(f"A média de idade do grupo é: {media_idade}")
print(f"O(s) homem(ns) mais velho(s) tem {H_maior_idade} anos e se chama(m): {', '.join(nome_H_mais_velho)}")
