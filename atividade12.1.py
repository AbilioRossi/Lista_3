# Faça um programa para imprimir:
# 1
# 2 2
# 3 3 3
# .....
# n n n n n n ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def trianguloNumetrico():
    n = int(input("Insira um numero: "))
    for i in range(1,n+1):
        lista = []
        for e in range(i):
            lista.append(i)
        print(*lista)

trianguloNumetrico()


