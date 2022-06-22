# Faça um programa que leia duas matrizes A e B 2x2 de inteiros,
# e imprima a matriz C que é a soma das matrizes A e B.

from random import randint
def printMatriz(matriz):
    for i in range(len(matriz)):
        print(*matriz[i])
    print("\n")

a = []
b = []
c = []

for i in range(2):
    listaA = []
    listaB = []
    for e in range(2):
        listaA.append(randint(1,9))
        listaB.append(randint(1,9))
    a.append(listaA)
    b.append(listaB)
printMatriz(a)
printMatriz(b)

for i in range(2):
    soma = []
    for e in range(2):
        soma.append(a[i][e] + b[i][e])
    c.append(soma)
printMatriz(c)