def fatorial(numero=1, show=False):
    """
    :parâm numero: O número a ser calculado.
    :parâm show: (opcional) Se não for passado, imprime apenas o número. Se for, imprime a conta do fatorial.
    :return: O valor do fatorial do número passado.
    """
    fatorial_num = 1
    for contador in range(numero, 0, -1):
        if show == True:
            print(contador, end='')
            if numero == 1:
                print(' x 1', end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial_num *= contador
    return fatorial_num