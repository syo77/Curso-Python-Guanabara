"""
Tratamento de exceções em Python
"""

try:
    print()
    print("--------------------------")
    print("try".center(26))
    print("'OPERAÇÃO'".center(26))
    print("--------------------------")
    print("Tente executar o código que pode causar um erro")
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    resultado = numero1 / numero2
except ZeroDivisionError:
    print()
    print("--------------------------")
    print("except nome do erro:".center(26))
    print("'FALHOU'".center(26))
    print("--------------------------")
    print("Este bloco será executado se ocorrer uma ZeroDivisionError")
    resultado = "Divisão por zero não é permitida"
    print(f"Resultado do erro (esse foi atribuído pelo programador): {resultado}")
else:
    print()
    print("--------------------------")
    print("else".center(26))
    print("'DEU CERTO'(opcional)".center(26))
    print("--------------------------")
    print("Este bloco será executado se não ocorrer nenhuma exceção")
    print("Operação bem-sucedida")
    print(f"Resultado da operação: {resultado}")
finally:
    print()
    print("--------------------------")
    print("finally".center(26))
    print("'CERTOU ou FALHA'(opcional)".center(26))
    print("--------------------------")
    print("Este bloco será executado independentemente de uma exceção ter ocorrido ou não")
    print("Fim do tratamento de exceções")
print()
print("%%%%%%%%%%%% Exceção genérica %%%%%%%%%%%%")
try:
    print()
    print("--------------------------")
    print("try".center(26))
    print("--------------------------")
    print("Tente executar o código que pode causar um erro")
    numero3 = int(input("Digite o primeiro número: "))
    numero4 = int(input("Digite o segundo número: "))
    resultado = numero3 / numero4
except Exception as e:
    print()
    print("--------------------------")
    print("except Exception as e".center(26))
    print("--------------------------")
    print(f"Exceção genérica (esse foi atribuído pelo python): {e}")
    print(f"Outro método, por classe (também atribuído pelo python)")
    print(f"O erro encontrado foi {e.__class__}")
else:
    print()
    print("--------------------------")
    print("else".center(26))
    print("--------------------------")
    print("Programa bem sucedido")
    print("Não houve exceção genérica")
print()
print("%%%%%%%%%%%% Várias exceções %%%%%%%%%%%%")
try:
    print()
    print("-------------------------------------")
    print("try".center(37))
    print("-------------------------------------")
    print("Tente executar o código que pode causar um erro")
    numero5 = int(input("Digite o primeiro número: "))
    numero6 = int(input("Digite o segundo número: "))
    lista = [7, 12]
    resultado = numero5 / numero6
    print(lista[19])
except (ValueError, TypeError):
    print()
    print("-------------------------------------")
    print("except (ValueError, TypeError):".center(37))
    print("-------------------------------------")
    print("Ocorreu um problema no tipo de dado que você forneceu!")
except ZeroDivisionError:
    print()
    print("-------------------------------------")
    print("except ZeroDivisionError:".center(37))
    print("-------------------------------------")
    print("Não é possível fazer uma divisão por zero!")
except KeyboardInterrupt:
    print()
    print("-------------------------------------")
    print("except KeyboardInterrupt:".center(37))
    print("-------------------------------------")
    print("O usuário não inseriu nenhum dado!")
except Exception as erro:
    print()
    print("-------------------------------------")
    print("except Exception as erro (__cause__):".center(37))
    print("-------------------------------------")
    print(f"Foi encontrado o erro: {erro.__cause__}")
else:
    print()
    print("-------------------------------------")
    print("else".center(37))
    print("-------------------------------------")
    print("Ocorreu tudo bem!")
print()
