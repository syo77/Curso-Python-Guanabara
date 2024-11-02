"""
Continuação do exercício 35
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
O programa deve mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
"""
r1 = float(input("Primeiro lado: "))
r2 = float(input("Segundo lado: "))
r3 = float(input("Terceiro lado: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulo ", end='')
    if r1 == r2 == r3:
        print("Equilátero.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Isósceles.")
    elif r1 != r2 != r3 != r1:
        print("Escaleno.")
else:
    print("Os segmentos acima NÃO PODEM SE FORMAR triângulo.")

