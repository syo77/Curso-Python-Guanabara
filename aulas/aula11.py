print("\nOlá, Mundo!")
print("\033[4;36;47mOlá, Mundo!\033[m")
print("""""Sintaxe Completa: /033[0;30;40mTEXTO DESEJADO/033[m
(Lembrar que é barra INVERTIDA, e não barra normal)""")

print("\nStyle:")
print("""0 - normal
1 - \033[1mnegrito\033[m
4 - \033[4msublinhado\033[m
7 - \033[7mnegado\033[m""")

print("\nText:")
print("""30 - sem cor
31 - \033[31mvermelho\033[m
32 - \033[32mverde\033[m
33 - \033[33mamarelo\033[m
34 - \033[34mazul escuro/roxo\033[m
35 - \033[0;35;40mmagenta\033[m
36 - \033[0;36mazul claro\033[m
37 - \033[0;37mcinza/branco\033[m""")

print("\nBack:")
print("""40 - sem fundo
41 - \033[41mvermelho\033[m
42 - \033[42mverde\033[m
43 - \033[43mamarelo\033[m
44 - \033[44mazul escuro/roxo\033[m
45 - \033[45mmagenta\033[m
46 - \033[46mazul claro\033[m
47 - \033[47mcinza/branco\033[m""")

print("Variáveis:")
print("Sintaxe: 'nome da var':'/033[m'")
print("Utiliza um dicionário para colocar as cores")
print("(Lembrar que é barra INVERTIDA, e não barra normal)")
nome = "Irineu"
cores = {'limpar':'\033[m', 'txtazul':'\033[34m', 'txtvermelho':'\033[31m', 'fndazul_claro':'\033[46m', 'txtamarelo':'\033[33m'}
print(f"Olá, {cores['txtvermelho']}{nome}{cores['limpar']}! {cores['fndazul_claro']}Muito prazer{cores['limpar']} em te {cores['txtamarelo']}conhecer{cores['limpar']}.  ")