"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

from os import system
system('cls')

dados = {}
total_gols = 0
lista_gols = []

dados['NOME'] = str(input("Nome: ")).title().strip()
while True:
    try:
        qtd_partidas = int(input("Quantidade de partidas: "))
        if qtd_partidas <= 0:
            print("INVÁLIDO. Digite uma quantidade válida...")
        else:
            break
    except ValueError:
        print("ERRO. Insira apenas números...")
for numero_partida in range(0, qtd_partidas):
    while True:
        try:
            gols = int(input(f"Quantos gols na partida {numero_partida+1}: "))
            if qtd_partidas < 0:
                print("INVÁLIDO. Digite uma quantidade válida...")
            else:
                break
        except ValueError:
            print("ERRO. Insira apenas números...")      
    lista_gols.append(gols)
dados['GOLS'] = lista_gols[:]
for qtd_gols in lista_gols:
    total_gols += qtd_gols
dados['TOTAL'] = total_gols
print(">"*19, "<"*19)
print(dados)
print(">"*19, "<"*19)
for chave, valor in dados.items():
    print(f"O campo {chave} tem o valor {valor}")
print(">"*19, "<"*19)
print(f"O jogador {dados['NOME']} jogou {qtd_partidas} partidas.")
# A lista está dentro de dados['GOLS'] (só pra marcar)
for indice, valor in enumerate(dados['GOLS']):
    print(f" >>> Na partida {indice+1}, fez {valor} gols")
print(f"Foi um total de {total_gols} gols")
print(">"*19, "<"*19)
print("FIM...")
print()
