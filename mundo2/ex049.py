"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o ussuário escolher, só que agora utilizando um laço for.
"""
num = int(input("Digite o número da tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i:>2} = {num*i:>2} ")
