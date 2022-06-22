# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

a = []
b = []

for i in range(10):
    a.append(int(input("Insira um numero: ")))
    b.append(a[i]**2)

soma = sum(b)
print("Os numeros escritos foram:", *a, "\nA soma de seus quadrados é:", soma)