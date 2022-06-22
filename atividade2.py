# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.

n = []
produto = 1

for i in range(5):
    n.append(int(input("Insira um numero: ")))
soma = sum(n)
for i in range(5):
    produto= produto*n[i]

print("Os 5 numeros digitados foram", *n,"\nA soma deles é", soma,"\nE a multiplicação é", produto)