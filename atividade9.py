# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

nome = str(input("Insira o nome de usuario: "))
nome = nome.upper()
nome1 = ""

for i in range (len(nome)):
    nome1 = nome1+nome[i]
    print(nome1)