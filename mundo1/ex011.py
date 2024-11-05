"""
Faça um programa que leia a largura e a altura de uma parede e mostre a área da parede e a quantidade de litros de tinta necessários para pintar a parede.
- Considere que 1 litro de tinta pinta 2m² de parede
"""
largura = float(input("Digite a largura da parede(em metros): "))
altura = float(input("Digite a altura da parede(em metros): "))
area = largura*altura
litro_tinta = area/2
print(f"Uma parede de {largura}m por {altura}m tem uma área de {area}m²")
print(f"É necessário de {litro_tinta} litro(s) de tinta para pintar a parede")