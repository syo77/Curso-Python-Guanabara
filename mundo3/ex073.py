"""
Cria uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
"""
from os import system
system('cls')

times_2024 = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Cruzeiro','Internacional', 'Fortaleza', 'Corinthians', 'Cuiabá', 'Bahia', 'Goiás', 'Coritiba', 'América-MG', 'Vasco', 'Santos', 'Chapecoense')
print("Os times são: ")
posicao = 1
iterar = 0
tamanho = len(times_2024)
while iterar < tamanho:
    print(f"{posicao}º: {times_2024[iterar]}")
    iterar += 1
    posicao += 1
# poderia ser usado o "for" com 'posicao' e "enumerate"
print("\n")
print("Os 5 primeiros colocados são: ")
for posicao, time in enumerate(times_2024[:5], start=1):
    print(f"{posicao}º: {time}")
print("\n")
print("Os 4 últimos colocados são: ")
total_times = len(times_2024)
for posicao, time in enumerate(times_2024[-4:], start=total_times-3):
    print(f"{posicao}º: {time}")
print("\n")
print("Em ordem alfabética: ")
print('\n'.join(sorted(times_2024)))
print("\n")
if 'Chapecoense' in times_2024:
    print(f"A Chapecoense está na {times_2024.index('Chapecoense')+1}ª colocação")
else:
    print("A chapecoense não está na lista")
print("\n")
