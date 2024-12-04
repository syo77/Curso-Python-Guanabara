"""
Crie um programa que leia dois valores e mostre um menu como o abaixo:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
Seu programa deverá realizar a operação solicitada em cada caso
"""
from time import sleep
numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
maior = 0
resultado = 0
# operacao = 0; começar com a operacao valendo 0
finalizar = False # pode apagar essa variavel
while not finalizar: # e colocar o while operacao != 5:
    operacao = int(input("""Diga a operação que deseja fazer:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
Digite: """))
    if operacao == 1:
        resultado = numero1 + numero2
        print(f"A soma de {numero1} + {numero2} é igual a: {resultado}")
    elif operacao == 2:
        resultado = numero1 * numero2
        print(f"A multiplicação de {numero1} x {numero2} é igual a: {resultado}")
    elif operacao == 3:
        if numero1 > numero2:
            maior = numero1
            print(f"Dentre os números {numero1} e {numero2} o maior deles é {maior}")
        elif numero2 > numero1:
            maior = numero2
            print(f"Dentre os números {numero1} e {numero2} o maior deles é {maior}")
        elif numero1 == numero2:
            maior = numero1
            print(f"Os dois números são iguais e tem o valor {maior}")    
    elif operacao == 4:
        numero1 = int(input("Digite um novo número: "))
        numero2 = int(input("Digite outro novo número: "))
        print(f"Os novos números são: {numero1}, {numero2}")
    elif operacao == 5:
        print("Saindo do programa...")
        # seguindo a lógica das opções de código nos comentários lá em cima: 
        finalizar = True # remover essa variável, pois quando operacao == 5, o programa finaliza
    else:
        print("Número inválido. Tente novamente!")
    print("=-=" * 20)
    sleep(0.7)