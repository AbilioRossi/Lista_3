# Faça um programa que leia as dimensões de duas matrizes A e B,
# e depois leia as duas matrizes (os elementos devem ser inteiros).
# Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes.
# Imprima as matrizes A, B e a matriz resultante da multiplicação.

from random import randint
def printMatriz(matriz):
    for i in range(len(matriz)):
        print(*matriz[i])
def criarMatriz(matriz, nome):
    coluna = int(input("Quantas colunas tem a matriz {}?".format(nome)))
    linha = int(input("Quantas linhas tem a matriz {}".format(nome)))
    for i in range(linha):
        lista = []
        for e in range(coluna):
            lista.append(randint(1,9))
        matriz.append(lista)

a = []
b = []
criarMatriz(a,"A")
criarMatriz(b,"B=")
print("Matriz A:")
printMatriz(a)
print("Matriz B:")
printMatriz(b)

c = []
if len(a)==len(b) and len(a[1])==len(b[1]):
    for i in range(len(a[1])):
        multi = []
        for e in range(len(a)):
            multi.append(a[i][e] * b[i][e])
        c.append(multi)
    print("Matriz C:")
    printMatriz(c)
