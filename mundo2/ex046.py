from time import sleep
"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de aritifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
for n in range(10, -1, -1):
    print(n)
    sleep(1)
print("Feliz ano novo!")