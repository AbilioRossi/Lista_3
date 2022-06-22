# Construa uma função que receba uma data no formato DD/MM/AAAA
# e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def data(dia, mes, ano):
    if mes==2 and dia>28:
        return "Data invalida"
    else:
        if mes==1:
            mes = "Janeiro"
        elif mes == 2:
            mes = "Fevereiro"
        elif mes == 3:
            mes = "Março"
        elif mes == 4:
            mes = "Abril"
        elif mes == 5:
            mes = "Maio"
        elif mes == 6:
            mes = "Junho"
        elif mes == 7:
            mes = "Julho"
        elif mes == 8:
            mes = "Agosto"
        elif mes == 9:
            mes = "Setembro"
        elif mes == 10:
            mes = "Outubro"
        elif mes == 11:
            mes = "Novembro"
        elif mes == 12:
            mes = "Dezembro"
        else:
            mes = "NULL"

        if mes == "NULL":
            return "Data invalida"
        else:
            return "{} de {} de {}".format(dia, mes, ano)

data1 = str(input("Insira a data: "))
data1 = data1.split("/")

dia = int(data1[0])
mes = int(data1[1])
ano = int(data1[2])

data = data(dia, mes, ano)

print(data)