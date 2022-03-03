dia = int(input())
mes = int(input())

def EstacaoAno(dia, mes):
    if dia >= 21 and mes == 9 or 1 <= dia <= 31 and 9 < mes < 12 or 1 <= dia <= 20 and mes == 12:
        return('PRIMAVERA')
    elif dia >= 21 and mes == 12 or 1 <= dia <= 31 and 1 < mes < 3 or 1 <= dia <= 20 and mes == 3:
        return('VERAO')
    elif dia >= 21 and mes == 3 or 1 <= dia <= 31 and 3 < mes < 6 or 1 <= dia <= 20 and mes == 6:
        return('OUTONO')
    elif dia >= 21 and mes == 6 or 1 <= dia <= 31 and 6 < mes < 9 or 1 <= dia <= 20 and mes == 9:
        return('INVERNO')


print(EstacaoAno(dia, mes))