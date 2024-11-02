"""
Desenvolva ma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite sua altura em METROS: "))
imc = peso / altura**2
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
# elif imc >= 18.5 and imc < 25:
#     print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
# elif imc >= 25 and imc < 30:
#     print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
# elif imc >= 30 and imc < 40:
#     print("Obesidade")
else:
    print("Obesidade mórbida")
