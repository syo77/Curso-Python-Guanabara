from os import system
system('cls')

pessoas = {'nome':'Yuri', 'sexo':'M', 'idade':19}
declaracao_dicionario = dict()

print()

print(pessoas['nome'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print()

print("As chaves são: ")
for i in pessoas.keys():
    print(i, end='  ')

print()
print()

print("Os valores são: ")
for i in pessoas.values():
    print(i, end='  ')

print()
print()

print("Os itens separados são: ")
for k, v in pessoas.items():
    print(f"Chave: {k}. Valor: {v}")

print()

print("Os itens juntos são: ")
for i in pessoas.items():
    print(f"{i}")

print()

del pessoas['sexo']
print("Removi a chave 'sexo'")
for i in pessoas.items():
    print(f"Os itens agora são: {i}")

print()

pessoas['idade'] = 99
print("Atualizei idade para 99 anos")
for k, v in pessoas.items():
    print(f"{k} = {v}")

print()
pessoas['peso'] = 63.5
print("Adicionei a chave peso")
for k, v in pessoas.items():
    print(f"{k} = {v}")

print()

print("--- Dicionário dentro da lista")
brasil = []
dicionario1_dentro_lista = {'uf':'Distrito Federal', 'sigla':'DF'}
dicionario2_dentro_lista = {'uf':'Bahia', 'sigla':'BA'}
brasil.append(dicionario1_dentro_lista)
brasil.append(dicionario2_dentro_lista)
print("-- Dicionário 1")
print(dicionario1_dentro_lista)
print("-- Dicionário 2")
print(dicionario2_dentro_lista)

print()

print("Lista com dicionário dentro")
print(brasil)

print()

print("Imprimindo dados da *LISTA*")
print(f"Brasil[0]: {brasil[0]}")
print(f"Brasil[1]: {brasil[1]}")

print()

print("Imprimindo dados do *DICIONÁRIO*")
print(f"Brasil[0]['uf']: {brasil[0]['uf']}-{brasil[0]['sigla']}")
print(f"Brasil[1]['uf']: {brasil[1]['uf']}-{brasil[1]['sigla']}")

estado = {}
país = []
for contador in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: ")).upper()
    estado['sigla'] = str(input("Sigla do Estado: ")).upper()
    país.append(estado.copy())
print()
print("Imprimindo a lista")
print(país)
for estado in país:
    for valor in estado.values():
        print(valor, end=' ')
    print()

print()
