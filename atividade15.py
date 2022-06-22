# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’,
#  se seu argumento for zero ou negativo.

# poun vem de Positivo OU Negativo
def poun(a):
    if a>0:
        valor = "P"
    else:
        valor= "N"
    print(valor)

n = int(input("Insira um numero: "))

poun(n)