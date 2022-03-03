media = float(input())
faltas = int(input())

def classificaAluno(media, faltas):
    if 9.5 > media >= 7 and faltas < 11:
        return('APROVADO')
    elif media >= 9.5 and faltas < 11:
        return('APROVADO COM LOUVOR')
    elif media < 7 and faltas < 11:
        return('REPROVADO')
    elif media > 7 and faltas > 10:
        return('REPROVADO POR FALTAS')


print(classificaAluno(media, faltas))
