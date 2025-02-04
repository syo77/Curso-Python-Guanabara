def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mINVÁLIDO. Digite um número inteiro válido...\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número...\033[m')
            return 0
        else:
            return numero



def imprimir_linha(tamanho=45):
    return '-'*tamanho



def cabecalho_menu(mensagem):
    print(imprimir_linha())
    print(mensagem.center(50))
    print(imprimir_linha())



def menu(lista):
    cabecalho_menu('\033[36mCADASTRO DA BÍBLIA\033[m')
    contador = 0
    while contador < len(lista):
        print(f'\033[35m{contador+1}\033[m - \033[34m{lista[contador]}\033[m')
        contador += 1
    print(imprimir_linha())
    opcao = leiaInt('\033[32mEscolha uma das opções:\033[m ')
    return opcao
