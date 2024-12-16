"""
Crie um programa que leia vários número inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

parar = False
contador = 0
soma = 0

while not parar:
  numero = int(input("Digite um número [999 para parar]: "))
  if numero == 999:
    parar = True
  if numero != 999:
    soma += numero
    contador += 1
print(f"Você digitou {contador} números e a soma deles é igual a {soma}")
print('¬¬¬'*10)
print(f"{'Acabou!':>19}")
print('¬¬¬'*10)