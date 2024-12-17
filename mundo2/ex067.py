"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    contador_interno = 1
    numero = int(input("Digite um número para a tabuada: "))
    if numero < 0:
        break
    print("---"*10)
    while contador_interno <= 10:
        resultado = numero * contador_interno
        print(f"{numero} X {contador_interno} = {resultado}")
        contador_interno += 1
    print("---"*10)
print("Programa encerrado.")
print("Muito obrigado!")

