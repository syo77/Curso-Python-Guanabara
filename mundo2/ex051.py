"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo+razao, razao):
    print(f"{i}", end=" → ")
print("FIM")