from os import system
system('cls')

# Funções parte 2

print(">>>>>>> AJUDA <<<<<<<")
print()
print("1: help('objeto que precisa de ajuda')", "sem o aspas simples")
print("OU")
print("2: print('objeto'.__doc__) ", "sem o aspas simples")
print()

print(">>>>>>> DOCSTRINGS <<<<<<<")
print()
print("1: Documentação de uma função criada pelo programador")
print("2: Usar aspas duplas três vezes dentro da função para criar a documentação")
def contador(inicio, fim, passo):
    """
|---------------------------------------------------------------|
|   Seja bem vindo(a) à primeira documentação feita por mim.    |
|                                                               |
|     Argumento 1: inicio - Digite o inicio da contagem.        |
|     Argumento 2: fim - Digite o fim da contagem.              |
|     Argumento 3: passo - Digite o passo de cada contagem.     |
|                                                               |
|     Ao final, a função exibe a contagem inserida.             |
|---------------------------------------------------------------|
    """
    contador = inicio
    while contador <= fim:
        print(contador, end=' ')
        contador += passo
    print("FIM")
help(contador)
print(">> FUNÇÃO <<")
print("""contador = inicio
while contador <= fim:
    print(contador, end=' ')
    contador += passo
print("FIM")""")
print()

print(">>>>>>> PARÂMETROS OPCIONAIS <<<<<<<")
print()
print("1: Para definir um parâmetro opcional, você deve atribuir um valor padrão na passagem dos parâmetros na criação da função")
def somar(a=0, b=0, c=0):
    soma = a+b+c
    print(f"A soma dos números (a = {a}) + (b = {b}) + (c = {c}) é igual a: {soma}")
somar(7, 12, 19)
somar(7, 12)
print()

print(">>>>>>> ESCOPO DE VARIÁVEIS <<<<<<<")
print()
print(">> VARIÁVEL LOCAL <<")
def teste1():
    x = 7
    print(f"Dentro da função a variável 'n' vale [{n1}]")
    print(f"Dentro da função a variável 'x' vale [{x}]")
# Fora da função
n1 = 12
teste1()
print(f"Fora da função a variável 'n' vale [{n1}]")
print(f"Fora da função a variável 'x' vale [indefinido] (por que é uma variável local da função 'teste')")
print()
print(">> VARIÁVEL GLOBAL <<")
def teste2(numero):
    global n2
    n2 = 19
    numero += 4
    c = 2
    print(f"Dentro da nova função a variável 'n' vale {n2}")
    print(f"Dentro da nova função a variável 'b' vale {numero}")
    print(f"Dentro da nova função a variável 'c' vale {c}")
n2 = 12
print(f"Fora e antes da nova função a variável 'n' vale {n2}")
teste2(n2)
print(f"Fora e depois da nova função a variável 'n' vale {n2}")
print()

print(">>>>>>> RETORNANDO VALORES <<<<<<<")
print()
print("""def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
somar(7, 12, 19)""")
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
print(f"O valor retornado é: {somar(7, 12, 19)}")










