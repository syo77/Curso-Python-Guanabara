n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
sm = n1+n2
sb = n1-n2
mt = n1*n2
dv = n1/n2
di = n1//n2
pt = n1**n2
print(f"""As operações são:
Soma: {sm}
Subtração: {sb}
Multiplicação: {mt}
Divisão: {dv:.3f}
Divisão Inteira: {di}
Potência: {pt} """)
nome = input("Digite seu nome: ")
print(f"Olá {nome:=^20}!")



