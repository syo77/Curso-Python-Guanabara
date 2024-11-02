"""
Crie um programa em Python que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
# media = (nota1 + nota2) / 2
media_iesb = 0.4*nota1 + 0.6*nota2
print(f"A sua média foi {media_iesb:.2f}")
if media_iesb < 5.0:
    print("Você está reprovado!")
elif media_iesb >= 5.0 and media_iesb < 7.0:
    print("Você está de recuperação, estude!")
elif media_iesb >= 7.0:
    print("Você está aprovado")
