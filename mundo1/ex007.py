"""
Faça um programa que leia duas notas de um aluno e calcule a média.
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = nota1*0.4 + nota2*0.6
print("""A primeira nota é: {:.2f}
A segunda nota é: {:.2f}
A média das notas no IESB é: {:.2f}""".format(nota1, nota2, media))