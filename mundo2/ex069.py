"""
Crie um programa que leia a idade e o sexo e várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""

pessoas_18mais = 0
homens = 0
mulheres_20mais = 0
continuar = ''
print("---"*10)
print(f"{'ANALISANDO CADASTRO':>24}")
print("---"*10)
while True:
    while True:
        try:
            idade = int(input("Digite a idade da pessoa: "))
            if idade > 0:
                break
            else:
                print("Inválido. Digite um número maior que zero!")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
    while True:
        sexo = str(input("Digite o sexo da pessoa [M/F]: ")).lower().strip()[0]
        if sexo in 'mf':
            break
        else:
            print("Inválido. Digite o sexo corretamente!")
    if idade >= 18:
        pessoas_18mais += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres_20mais += 1
    # while continuar not in 'sn':
        # continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        # if not in 'sn':
        #     print("Digite uma opção válida!")
    # if continuar == 'n':
    #     break
    while True:
        continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        if continuar in 'sn':
            break
        else:
            print("Inválido. Digite a opção corretamente!")
    if continuar == 'n':
        break
print("--=--"*15)
print(f"Você digitou {pessoas_18mais} pessoas com mais de 18 anos")
print(f"Você inseriu {homens} homens no cadastro")
print(f"Você enviou {mulheres_20mais} mulheres com mais de 20 anos para o cadastro")
print("--=--"*15)
