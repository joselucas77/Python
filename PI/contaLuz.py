consumo = float(input())
valor = consumo * 1.50
desconto = 0.15 * valor
descontoFinal = valor - desconto
print('Valor a ser pago: R$ %.2f reais' %valor)
print('Valor a ser pago com desconto: R$ %.2f reais' %descontoFinal)