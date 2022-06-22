# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas,
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

#Se passarem parametros fora dos estabelecidos, eles serem mudados para 10

def printMatriz(matriz):
    for i in range(len(matriz)):
        print(*matriz[i])

linha = int(input("Quantas linhas quer? "))
coluna = int(input("Quantas colunas quer? "))

if linha>20 or linha<1:
    linha=10
if coluna>20 or coluna<1:
    coluna=10

a = []

for i in range(linha):
    lista = []
    for e in range(coluna):
        lista.append("+")
    a.append(lista)
for i in range(coluna):
    a[0][i] = "-"
    a[linha-1][i] = "-"
for i in range(linha):
    a[i][0] = "|"
    a[i][coluna-1] = "|"

printMatriz(a)