"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. O programa retorna a quantidade de termos mostrados no programa completo.
"""

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

pa = primeiro_termo
contador = 0
finalizar = False
total_termos = 10

if razao != 0:
    while contador < 10:
        print(f"{pa}", end=' → ')
        pa += razao
        contador += 1
    print("PAUSA")
    while not finalizar:
        termos_mais = int(input("Digite quantos termos você quer mostrar a mais: "))
        # while termos_mais != 0
        if termos_mais != 0:
            contador = 0
            while contador < termos_mais:
                print(f"{pa}", end=' → ')
                pa += razao
                contador += 1
                total_termos += 1
            print("PAUSA")
        else:
            finalizar = True
            print("------------------------------------------------")
            print(f"O programa finalizou com {total_termos} termos exibidos")
            print(" --- Fim do programa --- ")
        # sugestão de código: trocar o incrementador do total_termos do if/while por pelo código abaixo. 
        # total_termos += termos_mais *(fora do else)*
else:
    print(" --- Fim do programa --- ")
    print("A razão da PA é 0 (zero)")