"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
distancia = int(input("Digite a distância da viagem: "))
if distancia <= 200:
    preco = float(distancia * 0.50)
    
else:
    preco = float(distancia * 0.45)
print(f"O preço de uma viagem de {distancia}Km é R${preco:.2f}!")