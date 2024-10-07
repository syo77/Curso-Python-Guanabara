"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
numero = randint(0, 5)
numero_user = int(input("Digite um número de 0 a 5: "))
if numero == numero_user:
    print("Você venceu, PARABÉNS!")
else:
    print("Você perdeu, TENTE NOVAMENTE!")