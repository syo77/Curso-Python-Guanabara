"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
"""
km = int(input("Quantidade de Km rodados: "))
dias = int(input("Quantos dias ele foi alugado: "))
preco = dias*60 + km*0.15
print(f"""O carro rodou {km}km em {dias} dia(s)
Portanto o preço do aluguel é R${preco:.2f}""")