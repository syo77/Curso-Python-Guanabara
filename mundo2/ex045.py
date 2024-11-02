from random import randint
"""
Pedra, papel, tesoura
"""
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
jogador = int(input("""Escolha uma das opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Digite: """))
print("-=-"*10)
print(f"Computador jogou {itens[computador]}")
print(f"jogador jogou {itens[jogador]}")
print("-=-"*10)
if computador == 0: # Pedra
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador ganhou")
    elif jogador == 2:
        print("Computador ganhou")
    else:
        print("Opção inválida, tente novamente!")
elif computador == 1: # Papel
    if jogador == 0:
        print("Computador ganhou")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador ganhou")
    else:
        print("Opção inválida, tente novamente!")
elif computador == 2: # Tesoura
    if jogador == 0:
        print("Jogador ganhou")
    elif jogador == 1:
        print("Computador ganhou")
    elif jogador == 2:
        print("Empate")
    else:
        print("Opção inválida, tente novamente!")










