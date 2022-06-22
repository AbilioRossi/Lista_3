# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical

nome = str(input("Insira o nome de usuario: "))
nome = nome.upper()

for i in range(len(nome)):
    print(nome[i])