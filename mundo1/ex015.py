km = int(input("Quantidade de Km rodados: "))
dias = int(input("Quantos dias ele foi alugado: "))
preco = dias*60 + km*0.15
print(f"""O carro rodou {km}km em {dias} dia(s)
Portanto o preço do aluguel é R${preco:.2f}""")