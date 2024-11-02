"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.
"""
frase = input("Digite sua frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("É um palíndromo")
    print(f"{junto} {inverso}")
    # if junto == junto[::-1]:
    #     print("É palíndromo")
    #     print(f"{junto}")
else:
    print("Não é palíndromo")
    print(f"{junto} {inverso}")

print("==="*20)
print("Meu jeito".center(60))
print("==="*20)

if junto == junto[::-1]:
    print("É um palíndromo")
    print(f"{junto} {junto[::-1]}")
else:
    print("Não é um palíndromo")
    print(f"{junto} {junto[::-1]}")
