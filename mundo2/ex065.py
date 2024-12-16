"""
Crie um programa que leia vários números inteiros pelo teclado. No final a execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

finalizar = False

soma = 0
contador = 0
media = 0
maior = 0
menor = 0

while not finalizar:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
    finalizar2 = False
    while not finalizar2:
        parar = str(input("Deseja continuar? [S/N]: ")).strip()[0]
        if parar.lower() in 'sn':
            finalizar2 = True
        else:
            print("Inválido. Insira o valor correto!")
    if parar.lower() == 'n':
        finalizar = True
        media = soma / contador
    if contador == 1:
        maior = numero
        menor = numero
        # maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f"Você digitou {contador} número(s) e a média entre eles é: {media:.2f}")
print(f"O maior número digitado foi '{maior}' e o menor foi '{menor}'")
print("¬¬¬"*10)
print("      Programa finalizado")
print("¬¬¬"*10)
