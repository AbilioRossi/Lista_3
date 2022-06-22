# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores

from random import randint
a = []
b = []
c = []

for i in range(10):
    a.append(randint(1,10))
    b.append((randint(1,10)))

for i in range(10):
    c.append(a[i])
    c.append(b[i])

print("Vetor 1:", *a, "\nVetor 2:", *b, "\nVetor 3:", *c)