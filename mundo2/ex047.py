from time import sleep
"""
Crie um programa que mostre na tela todos o números pares que estão no intervalo entre 1 e 50
"""

for i in range(1, 51):
    if i % 2 == 0:
        # print(f"{i}", end=' ')
        print(i)
        sleep(0.3)