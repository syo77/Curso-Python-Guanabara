from os import system
system('cls')

lanche = ('Pizza', 'Hamburguer', 'Suco', 'Pudim')
for c in range(0, 4):
    tamanho = len(lanche[c])
    for i in range(0, tamanho):
        print(lanche[c][i])
    print('')
