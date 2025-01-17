"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (esse é opcional)
Adicione também as docstrings.
"""

from os import system
system('cls')

def validar_opcao(mensagem):
    """
    Função para validar entradas do tipo 'S' ou 'N'.
    :param mensagem: Mensagem a ser exibida ao usuário.
    :return: Retorna 's' ou 'n' conforme a entrada do usuário.
    """
    while True:
        opcao = input(mensagem).lower().strip()[0]
        if opcao in 'sn':
            return opcao
        print("\033[31mINVÁLIDO. Digite apenas S ou N...\033[m")

def notas(*n, sit=False):
    """
    Recebe várias notas e retorna os dados: maior nota, menor nota, média da turma, situação (opcional) em um dicionário.
    Mostra a situação se o 'sit' for True.
    :parâm: n - Recebe várias notas
    :parâm: sit - Parâmetro opcional que indica a situação
    """
    from time import sleep
    # maior = max(n)
    maior = 0
    # menor = min(n)
    menor = 0
    soma_notas = 0
    # qtd_notas = len(n)
    qtd_notas = 0
    dicionario_notas = {}
    for posicao, nota in enumerate(n):
        if posicao == 0:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        qtd_notas += 1
        soma_notas += nota
    # media = sum(n) / len(n)
    media = soma_notas / qtd_notas
    situacao = ''
    if media >= 7 and media <= 10:
        situacao = 'EXCELENTE'
    elif media >= 5:
        situacao = 'OK'
    elif media >= 3:
        situacao = 'RECUPERAÇÃO'
    else:
        situacao = 'REPROVADO'
    dicionario_notas['QTD NOTAS'] = qtd_notas
    dicionario_notas['MAIOR'] = maior
    dicionario_notas['MENOR'] = menor
    dicionario_notas['MEDIA'] = round(media, 2)
    if sit:
        dicionario_notas['SITUAÇÃO'] = situacao
    sleep(1)
    return dicionario_notas
n_notas = []
situacao = False
print("\033[30;46m>>>>>>> ANALISADOR DE NOTAS <<<<<<<\033[m")
mostrar_ajuda = validar_opcao("\033[30mDeseja mostrar ajuda? [S/N]: \033[m")
if mostrar_ajuda == 's':
    print(help(notas),end='')
    print()
while True:
    while True:
        try:
            digitar_nota = int(input("\033[30mDigite a sua nota: \033[m"))
            if digitar_nota >= 0 and digitar_nota <= 10:
                n_notas.append(digitar_nota)
                print("\033[32mCadastrado...\033[m")
                break
            print("\033[31mINVÁLIDO. Digite a nota corretamente...\033[m")
        except ValueError:
          print("\033[31mERRO. Digite apenas números...\033[m")
    continuar_notas = validar_opcao("\033[30mDeseja continuar adicionando? [S/N]: \033[m")
    if continuar_notas == 'n':
        break
mostrar_situacao = validar_opcao("\033[30mDeseja mostrar a situação? [S/N]: \033[m")
if mostrar_situacao == 's':
    situacao = True
print()
print("\033[30;42m>>>>>>> OBTENDO RESULTADOS <<<<<<<\033[m")
print(notas(*n_notas, sit=situacao))
print()
