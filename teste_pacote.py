from pacotes.funcoes_numericas import numeros
from pacotes.funcoes_strings import strings1

print(numeros.dobro(4))

print(numeros.numero_mais_um(6))
print(numeros.numero_mais_um(11))

n_lista = [5, 4, 2, 6, 8, 10, 9, 11, 12, 19, 7]
numeros.pares(*n_lista)

print(strings1.maiusculo("programando em python"))