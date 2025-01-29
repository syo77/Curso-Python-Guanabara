def dobro(numero):
    return numero*2

def numero_mais_um(numero):
    return numero + 1

def pares(*numeros):
    numeros_pares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    print(numeros_pares)
print()