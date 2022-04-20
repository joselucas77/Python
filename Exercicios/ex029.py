vel = float(input('Qual a veloscidade atual do carro? '))
if vel > 80:
    multa = (vel-80)*7
    print('MULTADO! você exedeu o limite permitido de 80KM/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')