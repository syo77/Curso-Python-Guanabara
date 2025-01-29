def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"\033[0;31mINVÁLIDO: '{entrada}' é um valor inválido...\033[m")
        else:
            value = True
            return float(entrada)