# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = []

for i in range(5):
    ia = []
    ia.append(int(input("Insira a idade da {}° pessoa: ".format(i+1))))
    ia.append(float(input("Insira a altura da {}° pessoa: ".format(i+1))))
    pessoas.append(ia)

pessoas.reverse()
for i in range (5):
    print("\nIdade:", pessoas[i][0], "\nAltura:", pessoas[i][1])