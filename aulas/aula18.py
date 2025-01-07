"""
Listas compostas
"""
from os import system
system('cls')

teste = []

teste.append('Yuri')
teste.append(19)

pessoas = []

pessoas.append(teste[:])
print(teste)

teste[0] = 'Marina'
teste[1] = 18
pessoas.append(teste[:])

print(pessoas)

pessoas2 = [["Bruno", 30], ["Diego", 28], ["Lucas", 24], ["Mateus", 27], ["Gabriel", 26]]

for p in pessoas2:
    print(f"{p[0]}, você tem {p[1]} anos")

pessoas3 = []
dado = []

for contador in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    pessoas3.append(dado[:])
    dado.clear()
print(pessoas3)

total_maior = total_menor = 0

for pessoa in pessoas3:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade.")
        total_maior += 1
    else:
        print(f"{pessoa[0]} é menor de idade.")
        total_menor += 1
print(f"Há {total_maior} pessoa(s) maior(es) e {total_menor} pessoa(s) menor(es) de idade.")
