"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
"""
soma = 0
contador = 0
for i in range(1, 501, 2): # for i in range(1, 501):
    # if i % 2 != 0:
    #     if i % 3 == 0:
    #         soma += i
    #         contador += 1
    if i % 3 == 0:
        soma += i
        contador += 1
print(f"A soma de todos os {contador} valores é {soma}")