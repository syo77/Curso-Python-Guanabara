from os import system
system('cls')
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Digite uma posição da sequência de fibonacci: "))
print(f"O número da {n}º posição da sequência de fibonacci é: ", end='', flush=True)
print(fibonacci(n), flush=True)
print()

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(f"fibonacci 1000: {fibonacci(1000)}")
print()

try:
    resultado = 10 / int(input("Digite um número: "))
    print(resultado)
except Exception as erro_generico:
    print(f"Erro inesperado: {erro_generico}")

print()
