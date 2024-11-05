"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
import math
print("\nForma algébrica")
cateto_op = float(input("Cateto oposto: "))
cateto_ad = float(input("Cateto adjacente: "))
hipotenusa = math.sqrt(cateto_op**2 + cateto_ad**2)
print(f"""\nCateto Oposto: {cateto_op:.2f}
Cateto Adjacente: {cateto_ad:.2f}
Hipotenusa: {hipotenusa:.2f}""")

print("\nForma Python")
hipotenusa2 = math.hypot(cateto_op, cateto_ad)
print(f"Pela forma Python, a hipotenusa é: {hipotenusa2:.2f}")







