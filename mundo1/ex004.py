"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
mensagem = input("Digite alguma coisa: ")
print("O tipo primitivo é:",type(mensagem))
print("É alfanumérico?",mensagem.isalnum())
print("É alfabético?",mensagem.isalpha())
print("É número?",mensagem.isdigit())
print("Só tem espaços?",mensagem.isspace())
print("É minúsculo?",mensagem.islower())
print("É maiúsculo?",mensagem.isupper())
print("É capitalizado?",mensagem.istitle())