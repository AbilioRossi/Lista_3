# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
# e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto (taxaImposto,custo):
    custo = custo + ((custo*taxaImposto)/100)
    return custo

produto = float(input("Insira o preço do produta, no qual vai ser aplicado o imposto: "))
taxa = int(input("Insira a taxa do imposto: "))

print(somaImposto(taxa, produto))