"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

from time import sleep
from os import system
system('cls')
notas_total = []
temporario = []
media = 0
while True:
    nome = str(input("Nome: ")).title()
    temporario.append(nome)
    while True:
        try:
            nota1 = float(input("Nota 1: "))
            if nota1 < 0 or nota1 > 10:
                print("INVÁLIDO. Digite uma nota válida...")
            else:
                temporario.append(nota1)
                break
        except ValueError:
            print("ERRO. Digite um número...")
    while True:
        try:
            nota2 = float(input("Nota 2: "))
            if nota2 < 0 or nota2 > 10:
                print("INVÁLIDO. Digite uma nota válida...")
            else:
                temporario.append(nota2)
                break
        except ValueError:
            print("ERRO. Digite um número...")
    while True:
        continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        if continuar in 'sn':
            break
        else:
            print("INVÁLIDO. Tente novamente 'S' ou 'N'")
    notas_total.append(temporario[:])
    temporario.clear()
    if continuar == 'n':
        break
notas_total.sort()
print(f"    {'N°.':<7} {'NOME':<12} {'MÉDIA':>7}")
print("-----"*7)
for posicao, elemento in enumerate(notas_total, start=1):
    media = elemento[1]*0.4 + elemento[2]*0.6
    print(f"   {f'[ {posicao} ]':<7}  {elemento[0]:<12} {f'{media:.2f}':>7}")
print("-----"*7)
print()
while True:
    try:
        parar_notas = int(input("Digite o número do aluno para mostrar as notas. (999 para parar): "))
        if parar_notas == 999:
            print("Encerrando...")
            sleep(0.5)
            print("Acabou!")
            break
        if parar_notas > len(notas_total) or parar_notas < 1:
            print("ERRO. Digite um aluno válido.")
        else:
            print(f"As notas do aluno {notas_total[parar_notas-1][0]} são: {notas_total[parar_notas-1][1:]}")
            print()
    except ValueError:
        print("ERRO. Insira o número de um aluno.")
print()
