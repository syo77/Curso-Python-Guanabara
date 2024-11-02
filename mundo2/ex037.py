"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
"""
escolha = int(input("""Escolha qual conversão quer fazer:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
Digite: """))
if escolha == 1 or escolha == 2 or escolha == 3:
    numero_base_dez = int(input("Digite um número inteiro positivo: "))
    if escolha == 1:
        binario = bin(numero_base_dez)[2:]
        print(f"O número {numero_base_dez} em base binária é '{binario}'")
    elif escolha == 2:
        octal = oct(numero_base_dez)[2:]
        print(f"O número {numero_base_dez} em base octal é '{octal}'")
    elif escolha == 3:
        hexadecimal = hex(numero_base_dez)[2:]
        print(f"O número {numero_base_dez} em base hexadecimal é '{hexadecimal.upper()}'")
else:
    print("Valor inválido, tente novamente!")
