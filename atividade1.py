# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
notas = []
alunosAcima = []

for i in range(10):
    alunos.append(str(input("Insira o nome do aluno: ")))
    for a in range(1,5):
        notas.append(float(input("Insira a nota {} do aluno: ".format(a))))
    media = sum(notas)/4
    if media >= 7 :
        alunosAcima.append(alunos[i])
    notas.clear()
    print("\n")

print(len(alunosAcima), "alunos ficaram acima da média. seus nomes são:")
for i in range (len(alunosAcima)):
    print(alunosAcima[i])