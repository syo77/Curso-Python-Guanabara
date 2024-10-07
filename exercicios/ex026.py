"""Faça um programa que leia uma frase pelo teclado e mostre: 
Quantas vezes aparece a letra 'A'.
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez?
"""
frase = input("Digite sua frase: ").upper().strip()
print(f"Ocorrências de 'A': {frase.count("A")}")
print(f"Primeira ocorrência de 'A': {frase.find("A")+1}")
print(f"Última ocorrência de 'A': {frase.rfind("A")+1}")