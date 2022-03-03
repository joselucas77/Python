entrada = input()
valores = entrada.split()
num1 = float(valores[0])
num2 = float(valores[1])
num3 = float(valores[2])
num4 = float(valores[3])

def AnalizarSituacao(num1, num2, num3, num4):
    mp = ((num1*1) + (num2*2) + (num3*3) + (num4*4)) / 10
    if mp >= 9:
        return('aprovado com louvor')
    elif 9 > mp >= 7:
        return('aprovado')
    elif mp < 3:
        return('reprovado')
    elif 3 >= mp < 7:
        return('prova final')

print(AnalizarSituacao(num1, num2, num3, num4))