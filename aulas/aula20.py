from os import system
system('cls')

# Funções em python *( PARTE 1 )*

# Função básica

def linha():
    print("---"*19)

print()
print(" >>>>>>> PRINT <<<<<<<")
print()

print("---"*19)
print(f"{"ALGUMA COISA":>28}")
print("---"*19)
print("---"*19)
print(f"{"OUTRA COISA":>28}")
print("---"*19)
print("---"*19)
print(f"{"ALGUMA OUTRA COISA":>28}")
print("---"*19)

print()
print(" >>>>>>> FUNÇÃO <<<<<<<")
print()

linha()
print(f"{"ALGUMA COISA":>28}")
linha()
linha()
print(f"{"OUTRA COISA":>28}")
linha()
linha()
print(f"{"ALGUMA OUTRA COISA":>28}")
linha()

# Função com parâmetros

def mensagem(msg):
    print("---"*19)
    print(msg)
    print("---"*19)

print()
print(">>>>>>> FUNÇÃO COM PARÂMETROS <<<<<<<")
print()

# Chamando a função
mensagem("QUALQUER COISA")
# mensagem(input("Digite a mensagem que deseja passar: "))

print()
print(">>>>>>> PARTE PRÁTICA <<<<<<<")
print()

print("Código")
n1 = 7
n2 = 12
s = n1 + n2
print("""n1 = 7
n2 = 12
s = n1 + n2
print(f"{n1} + {n2} = {s}")""")
print("RESULTADO: ")
print(f"{n1} + {n2} = {s}")

print()
print("Função")
def somar_numeros(a, b):
    s = a + b
    print(f"A = {a} e B = {b}")
    print(f"{a} + {b} = {s}")
    print()
print("""def somar_numeros(a, b):
    s = a + b
    print(f"A = {a} e B = {b}")
    print(f"{a} + {b} = {s}")
    print()
somar_numeros(7, 12)""")
print("RESULTADO: ")
somar_numeros(7, 12)

print("Trocar a ordem")
print("somar_numeros(b=7, a=12)")
somar_numeros(b=7, a=12)

print(">>>>>>> DESEMPACOTADOR <<<<<<<")
print()
print("Diversos parâmetros")
print("""def contador(* num):
    print("Retorna uma tupla dos números: ", end='')
    print(num)
    print("Valores tirados da tupla: ")
    for valor in num:
        print(valor, end=' ')
    print("/||/")
    print()
contador(7, 12, 19)""")
def contador(* num):
    print("Retorna uma tupla dos números: ", end='')
    print(num)
    print("Valores tirados da tupla: ", end='')
    for valor in num:
        print(valor, end=' → ')
    print("/|/")
    print(f"Foram passados {len(num)} números")
    print()

print()
contador(7, 12, 19)
contador(30, 27)

print("Operador asterisco *")
print("Pode ser usado para desempacotar estruturas, como tuplas e listas")
print("contador(*[1, 2, 3, 4, 5, 6, 7])")
contador(*[1, 2, 3, 4, 5, 6, 7])

print("SOMANDO VALORES")
print("""def somar_varios_valores(* valores):
    soma = 0
    for numero in valores:
        soma += numero
    print(f"Somando os valores {valores}, temos {soma}")
somar_varios_valores(7, 12, 19)
somar_varios_valores(1, 2, 3, 4, 5)""")
print()
def somar_varios_valores(* valores):
    soma = 0
    for numero in valores:
        soma += numero
    print(f"Somando os valores {valores}, temos {soma}")
somar_varios_valores(7, 12, 19)
somar_varios_valores(1, 2, 3, 4, 5)
print()

print(">>>>>>> ITERAR E ALTERAR VALORES DE VARIÁVEIS <<<<<<<")
print()

print("""valores = [9, 5, 7, 6, 2, 12, 0, 3]
def dobrar_valores(lista):
    contador = 0
    while contador < len(lista):
        lista[contador] *= 2
        contador += 1
print(f"Valores antes: {valores}")
dobrar_valores(valores)
print(f"Valores depois: {valores}")""")

print()
print("PASSAGEM POR REFERÊNCIA: ")

print("""valores = [9, 5, 7, 6, 2, 12, 0, 3]
def dobrar_valores(lista):
    contador = 0
    while contador < len(lista):
        lista[contador] *= 2
        contador += 1
print(f"Valores antes: {valores}")
dobrar_valores(valores)
print(f"Valores depois: {valores}")""")

valores = [9, 5, 7, 6, 2, 12, 0, 3]
def dobrar_valores(lista):
    contador = 0
    while contador < len(lista):
        lista[contador] *= 2
        contador += 1
print()
print("RESULTADO: ")
print(f"Valores antes: {valores}")
dobrar_valores(valores)
print(f"Valores depois: {valores}")

print()
print("PASSAGEM POR VALOR: ")

print("""def passagem_valor(x):
    x *= 2
    print(f"Dentro da função: x = {x}")
x = 7
print(f"Antes de chamar a função: x = {x}")
passagem_valor(x)
print(f"Depois de chamar a função: x = {x}")""")
print()
print("RESULTADO: ")
def passagem_valor(x):
    x *= 2
    print(f"Dentro da função: x = {x}")
x = 7
print(f"Antes de chamar a função: x = {x}")
passagem_valor(x)
print(f"Depois de chamar a função: x = {x}")

print()
print("OBJETOS MUTÁVEIS POR VALOR: ")

print("""def mutaveis_valor(lista):
    # passar uma cópia do objeto mutável dentro do parâmetro
    lista = lista[:]
    lista.append(999)
    print(f"Dentro da função: {lista}")
lista = [1, 2, 3]
print(f"Antes da função: {lista}")
mutaveis_valor(lista)
print(f"Depois da função: {lista}")""")
print()
print("RESULTADO: ")
def mutaveis_valor(lista):
    # passar uma cópia do objeto mutável dentro do parâmetro
    lista = lista[:]
    lista.append(999)
    print(f"Dentro da função: {lista}")
lista = [1, 2, 3]
print(f"Antes da função: {lista}")
mutaveis_valor(lista)
print(f"Depois da função: {lista}")

print()