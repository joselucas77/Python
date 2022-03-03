hemis = int(input())
dia = int(input())
mes = int(input())

def EstacaoAnoSul(dia, mes):
    if dia >= 21 and mes == 9 or 1 <= dia <= 31 and 9 < mes < 12 or 1 <= dia <= 20 and mes == 12:
        return('PRIMAVERA')
    elif dia >= 21 and mes == 12 or 1 <= dia <= 31 and 1 < mes < 3 or 1 <= dia <= 20 and mes == 3:
        return('VERAO')
    elif dia >= 21 and mes == 3 or 1 <= dia <= 31 and 3 < mes < 6 or 1 <= dia <= 20 and mes == 6:
        return('OUTONO')
    elif dia >= 21 and mes == 6 or 1 <= dia <= 31 and 6 < mes < 9 or 1 <= dia <= 20 and mes == 9:
        return('INVERNO')


def EstacaoAnoNorte(dia, mes):
    if dia >= 21 and mes == 9 or 1 <= dia <= 31 and 9 < mes < 12 or 1 <= dia <= 20 and mes == 12:
        return('OUTONO')
    elif dia >= 21 and mes == 12 or 1 <= dia <= 31 and 1 < mes < 3 or 1 <= dia <= 20 and mes == 3:
        return('INVERNO')
    elif dia >= 21 and mes == 3 or 1 <= dia <= 31 and 3 < mes < 6 or 1 <= dia <= 20 and mes == 6:
        return('PRIMAVERA')
    elif dia >= 21 and mes == 6 or 1 <= dia <= 31 and 6 < mes < 9 or 1 <= dia <= 20 and mes == 9:
        return('VERAO')


if hemis == 0:
    print(EstacaoAnoNorte(dia, mes))
else :
    print(EstacaoAnoSul(dia, mes))