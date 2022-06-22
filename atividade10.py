# Faça um programa que leia uma matriz 3x3 de inteiros;
# e multiplique os elementos da diagonal principal da matriz por um número k.
# Imprima a matriz na tela antes e depois da multiplicação.

from random import randint
def printMatriz(matriz):
    for i in range(len(matriz)):
        print(*matriz[i])
a = []

for i in range(3):
    lista = []
    for e in range(3):
        lista.append(randint(1,9))
    a.append(lista)

printMatriz(a)

k = int(input("\nInsira o numero que quer multiplicar: "))

for i in range(3):
    a[i][i] = a[i][i]*k

printMatriz(a)