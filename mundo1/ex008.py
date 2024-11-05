"""
Faça um programa que receba um valor em metros e mostre a conversão para diferentes unidades de medida.
"""
metro = float(input("Digite um valor em metros: "))
km = metro/1000
hm = metro/100
dc = metro/10
dm = metro*10
cm = metro*100
mm = metro*1000
print(f"""O valor {metro} em metros corresponde:
{km} km
{hm} hm
{dc} dc
{dm} dm
{cm} cm
{mm} mm""")