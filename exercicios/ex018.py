from math import sin, cos, tan, radians
angulo = float(input("\nDiga o ângulo que deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"""\nO ângulo é: {angulo}°
O seno de {angulo:.2f}° é: {seno:.2f}
O cosseno de {angulo:.2f}° é: {cosseno:.2f}
A tangente de {angulo:.2f}° é: {tangente:.2f}""")







