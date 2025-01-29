def aumentar(valor = 0, desconto = 0):
    return valor + valor * (desconto / 100)

def diminuir(valor = 0, desconto = 0):
    return valor - valor * (desconto / 100)

def dobro(valor = 0):
    return valor * 2

def metade(valor = 0):
    return valor / 2

def formatar_moeda(valor = 0, moeda = 'R$'):
    formatador = f'{moeda}{valor:.2f}'
    if moeda == 'R$':
        return formatador.replace('.', ',')
    else:
        return formatador