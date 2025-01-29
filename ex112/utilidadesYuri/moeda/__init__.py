def aumentar(valor = 0, desconto = 0):
    return valor + valor * (desconto / 100)

def diminuir(valor = 0, desconto = 0):
    return valor - valor * (desconto / 100)

def dobro(valor = 0):
    return valor * 2

def metade(valor = 0):
    return valor / 2

def formatar_moeda(valor = 0, moeda = 'R$', formatar = False):
    if formatar == False:
        return f'{moeda}{valor}'
    else:
        formatador = f'{moeda}{valor:.2f}'
        if moeda == 'R$':
            return formatador.replace('.', ',')
        else:
            return formatador
    
def resumo(valor = 0, desconto1 = 0, desconto2 = 0):
    print("--"*19)
    print("RESUMO".center(38))
    print("--"*19)
    print("Valor passado: ".ljust(20), f'{formatar_moeda(valor, formatar=True)}')
    print("Dobro do valor: ".ljust(20), f'{formatar_moeda(dobro(valor), formatar=True)}')
    print("Metade do valor: ".ljust(20), f'{formatar_moeda(metade(valor), formatar=True)}')
    print(f"{desconto1}% de aumento: ".ljust(20), f'{formatar_moeda(diminuir(valor, desconto1), formatar=True)}')
    print(f"{desconto2}% de desconto: ".ljust(20), f'{formatar_moeda(diminuir(valor, desconto2), formatar=True)}')
    print("--"*19)
