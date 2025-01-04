"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

from os import system
system('cls')

palavras = ("caderno", "lapis", "caneta", "borracha", "estojo", "mochila", "regua", "apontador", "marcador", "papel", "livro", "computador", "teclado", "monitor", "mesa", "cadeira", "janela", "porta", "parede", "teto")

vogais = 'aeiou'

for palavra in palavras:
  printar_vogais = ''
  print(f"A palavra {palavra.upper()} tem as vogais ", end='')
  for vogal in palavra:
    if vogal in vogais and vogal not in printar_vogais:
      printar_vogais += vogal
  print(f"'{printar_vogais}'")
