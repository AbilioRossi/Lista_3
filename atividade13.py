# Faça um programa para imprimir:
# 1
# 1 2
# 1 2 3
# .....
# 1 2 3 ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def trianguloNumerico():
    lista = []
    n = int(input("Insira um numero: "))
    for i in range(1, n+1):
        lista.append(i)
        print(*lista)

trianguloNumerico()
