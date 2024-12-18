try:
    resultado = 10 / int(input("Digite um número: "))
    print(resultado)
except Exception as erro_generico:
    print(f"Erro inesperado: {erro_generico}")
