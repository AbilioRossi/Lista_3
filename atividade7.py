# Faça um programa que permita ao usuário digitar o seu nome;
# e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.

nome = str(input("Insira seu nome de usuario: "))
nome = nome.upper()

for i in range(-1, -(len(nome))-1, -1):
    print(nome[i],end="")
