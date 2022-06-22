# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

a = str(input("Insira uma frase: "))
b = str(input("Insira outra frase: "))

print("Tamanho de '{}': {} caracteres".format(a, len(a)), "\nTamanho de '{}': {} caracteres".format(b, len(b)))

if len(a)==len(b):
    print("As duas strings tem o mesmo tamanho")
else:
    print("As duas strings são de tamanhos diferentes")

if a == b :
    print("As duas strings possuem o mesmo conteudo")
else:
    print("As duas strings pussuem conteudos diferentes ")