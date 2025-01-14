"""
Faça um programa que tenha um função chamada escreva(), que receeba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá Mundo!)
Saida:
~~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~~
"""

from os import system
system('cls')

def escreva(mensagem):
    mensagem = str(input("Digite a sua mensagem: "))
    printar_linha = len(mensagem)+2
    print("~"*printar_linha)
    print(f"{f' {mensagem}'}")
    print("~"*printar_linha)
mensagem = ''
escreva(mensagem)
escreva(mensagem)
escreva(mensagem)

print()
