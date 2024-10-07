frase = "Curso em Video Python"
frase1 = "   Aprenda Python  "
print("""Fatiamento de string""")
print(f"\nfrase: {frase}")
print("frase[9]")
print(frase[9]) #Imprime o caractere 9 da string
print("frase[9:13]")
print(frase[9:13]) #Imprime a partir do caractere 9 até o 12, porque quando chega no 13 ele não imprime
print("frase[9:21:2]")
print(frase[9:21:2]) #Imprime do 9 ao 21, pulando de 2 em 2
print("frase[:5]")
print(frase[:5]) #Imprime do início da string até o caractere 5
print("frase[15:]")
print(frase[15:]) #Imprime do caractere 15 até o final da string
print("frase[9::3]")
print(frase[9::3]) #Imprime do caractere 9 até o final da string, pulando de 3 em 3
print("len(frase)")
print(len(frase)) #Imprime o tamanho da string
print("""frase.count("o")""")
print(frase.count("o")) #Imprime quantas vezes ocorre o a letra 'o'
print("""frase.count("o", 0,13)""")
print(frase.count("o", 0,13)) #Imprime as ocorrências de 'o' de 0 até 12, porque o 13 não imprime
print("""frase.find("deo")""")
print(frase.find("deo")) #Imprime as ocorrências de 'deo' dentro da string
print("""frase.find("iPhone")""")
print(frase.find("iPhone")) #Procura a string dada dentro da string principal e imprime '-1' se não achar
print(""""Curso" in frase""")
print("Curso" in frase) #Procura a string dada dentro da string principal e imprime True se achar ou False se não achar

print("""\nTransformações de strings""")
print("""frase.replace('Python', 'iPhone')""")
print(frase.replace("Python", "iPhone")) #Substitui a palavra "Python" por "iPhone"
print("frase.upper()") 
print(frase.upper()) #Transforma os caracteres da string em maiúsculos
print("frase.lower()")
print(frase.lower()) #Transforma os caracteres da string em minúsculos
print("frase.capitalize()")
print(frase.capitalize()) #Deixa apenas a primeira letra da string em maiúsculo
print("frase.title()") 
print(frase.title()) #Deixa todas as palavras da string com letra maiúscula. Isso ocorre devido ao python procurar os espaços dentro da string, então a partir de cada espaço ele coloca uma letra maiúscula
print("frase.strip()")
print("""frase com espaço:
   Aprenda Python  """)
print(f"""frase sem espaço:
{frase1.strip()}""") #Remove todos os espaços excedentes da string (espaços no começo e espaços no final)
print("frase.rstrip()")
print(frase1.rstrip()) #Remove apenas os espaço excedentes à direita
print("frase.lstrip()")
print(frase.lstrip()) #Remove apenas os espaços excedentes à esquerda
print("frase.split()")
fraseN = frase.split()
print(fraseN) #Faz uma divisão de cada palavra da string e os coloca em uma lista
dividido = frase.split()
print("""dividido = frase.split()
print(dividido [0])""")
print(dividido[0]) #Imprime a primeira palavra da string, por ser o primeiro elemento de uma lista
print("dividido[0] [3]")
print(dividido[0] [3]) #Imprime a letra 3 da primeira palavra
print("'-'.join(frase)")
print('-'.join(fraseN)) #Junta a string dividida separada por '-', se quiser que seja separada por espaços é só colocar assim: ' '