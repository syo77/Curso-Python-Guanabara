from datetime import date
current_year = date.today().year
"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
sexo = input("""\nDiga qual é o seu sexo 
[ M ] Masculino
[ F ] Feminino
Digite: """)
if sexo.upper() == 'M':
    ano_nasc = int(input("Digite o ano do seu nascimento: "))
    idade = current_year - ano_nasc
    print(f"\nQuem nasceu em {ano_nasc} tem {idade} anos em {current_year}.")
    if idade < 18:
        tempo = 18 - idade
        ano_alistamento = current_year + tempo
        print("O jovem ainda vai se alistar!")
        print(f"Ainda falta(m) {tempo} ano(s) para o alistamento.")
        print(f"Você deverá se alistar em {ano_alistamento}.")
    elif idade == 18:
        print("Está na hora de se alistar!")
    else:
        tempo = idade - 18
        ano_alistamento = current_year - tempo
        print("Passou da hora de se alistar!")
        print(f"Você deveria ter se alistado há {tempo} ano(s).")
        print(f"Seu ano de alistamento foi em {ano_alistamento}.")
elif sexo.upper() == 'F':
    print("\nO alistamento é voluntário!")
    ano_nasc = int(input("Digite o ano do seu nascimento: "))
    idade = current_year - ano_nasc
    tempo = 18 - idade
    print(f"\nQuem nasceu em {ano_nasc} tem {idade} anos em {current_year}")
    if ano_nasc < 2007:
        print("Você nasceu antes de 2007, não pode se alistar voluntariamente.")
    else:
        print("Você nasceu a partir de 2007, você pode se alistar voluntariamente.")
        print(f"Ainda faltam {tempo} ano(s).")
else:
    print("Escolha um opção válida!")
