"""
Escreve um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

vel_carro = int(input("Digite a velocidade do carro: "))
# vel_max = 80
if vel_carro > 80: # if vel_carro > vel_max:
    print(f"Você está a {vel_carro}Km/h e excedeu o limite de velocidade.")
    print("Você foi multado!")
    multa = float((vel_carro - 80) * 7) # multa = float((vel_carro - vel_max) * 7)
    print(f"A sua multa será de R${multa:.2f}")
else:
    print("""Tudo certo!
Siga sua viagem!""")

# Segundas opções ficarão como comentário