"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

DESAFIO 093: " Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. "

"""

from os import system
system('cls')

lista_dados = []
while True:
    total_gols = 0
    dados = {}
    lista_gols = []
    dados['NOME'] = str(input("Nome: ")).upper().strip()
    while True:
        try:
            dados['QTD_PARTIDAS'] = int(input("Quantidade de partidas: "))
            if dados['QTD_PARTIDAS'] <= 0:
                print("INVÁLIDO. Digite uma quantidade válida...")
            else:
                break
        except ValueError:
            print("ERRO. Insira apenas números...")
    for numero_partida in range(0, dados['QTD_PARTIDAS']):
        while True:
            try:
                gols = int(input(f"Quantos gols na partida {numero_partida+1}: "))
                if dados['QTD_PARTIDAS'] < 0:
                    print("INVÁLIDO. Digite uma quantidade válida...")
                else:
                    break
            except ValueError:
                print("ERRO. Insira apenas números...")      
        lista_gols.append(gols)
    while True:
        continuar = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
        if continuar in 'sn':
            break
        print("INVÁLIDO. Digite S ou N...")
    dados['GOLS'] = lista_gols[:]
    for qtd_gols in lista_gols:
        total_gols += qtd_gols
    dados['TOTAL'] = total_gols
    lista_dados.append(dados.copy())
    if continuar == 'n':
        break
print(">"*19, "<"*19)
print(lista_dados)
print(">"*19, "<"*19)
print(f"{'CÓDIGO':<8} {'NOME'} {'GOLS':>12} {'TOTAL':>25}")
print("---"*19)
for posicao, pessoa in enumerate(lista_dados):
    print(f"{f'{posicao+1}':>5}    {pessoa['NOME']:<12} {f'{pessoa['GOLS']}':<25} {pessoa['TOTAL']}")
print("---"*19)
while True:
    try:
        mostrar_dados = int(input("Digite o código do jogador que deseja mostrar (999 pra parar): "))
        if mostrar_dados == 999:
            print("Encerrando...")
            break
        if mostrar_dados > len(lista_dados) or mostrar_dados <= 0:
            print("INVÁLIDO. Digite um código válido...")
        else:                    # lista[indice a ser procurado][chave do dicionario]
            if mostrar_dados < len(lista_dados) or mostrar_dados >= 0:
                print(">"*19, "<"*19)
                print(f' >>> LEVANTAMENTO {lista_dados[mostrar_dados-1]['NOME']}')
                for contador_jogos, printar_gols in enumerate(lista_dados[mostrar_dados-1]['GOLS']):
                    print(f"No jogo {contador_jogos+1} fez {printar_gols} gols.")
                print()
    except ValueError:
        print("ERRO. Digite apenas números...")
print()
