from ex115.biblioteca.menu import cabecalho_menu

def validar_arquivo(nome):
    try:
        with open(f"ex115/{nome}", 'r', encoding="utf-8") as arquivo:
            arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(nome):
    try:
        with open(f"ex115/{nome}", 'w', encoding="utf-8") as arquivo:
            arquivo.close()
    except:
        print("ERRO. Não foi possível gerar o arquivo!")
    else:
        print(f"O arquivo {nome} foi criado com sucesso!")



def lerArquivo(nome):
    try:
        with open(f"ex115/{nome}", 'r', encoding="utf-8") as arquivo:
            cabecalho_menu('LISTA LIVROS CADASTRADOS')
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                dado[2] = dado[2].replace('\n', '')
                print(f"Livro: {dado[0]:<14}Capítulo: {dado[1]:<3}  Verso: {dado[2]}")
    except Exception as e:
        print(f"ERRO ao ler o arquivo... (motivo: {e})")
    else:
        arquivo.close()



def cadastrar(nome_arquivo, nome_livro='nenhum', capitulo_livro=1, verso_capitulo=1):
    try:
        with open(f"ex115/{nome_arquivo}", 'a', encoding="utf-8") as arquivo:
            arquivo.write(f'{nome_livro};{capitulo_livro};{verso_capitulo}\n')
    except:
        print("Ocorreu um ERRO na escrita dos dados...")
    else:
        print(f"Novo registro de {nome_livro} {capitulo_livro} adicionado!")



def remover_ultima_linha(nome_arquivo):
    from time import sleep
    try:
        with open(f"ex115/{nome_arquivo}", 'r', encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        if not linhas:
            print("O arquivo está vazio!")
        print("Removendo a última linha adicionada")
        sleep(1)
        with open(f"ex115/{nome_arquivo}", 'w', encoding="utf-8") as arquivo:
            arquivo.writelines(linhas[:-1])
        print("A última linha foi removida com sucesso!")
    except FileNotFoundError:
        print("\033[31mERRO. Arquivo não encontrado!\033[m")
    except Exception as e:
        print(f"\033[31mERRO inesperado: {e}\033[m")
