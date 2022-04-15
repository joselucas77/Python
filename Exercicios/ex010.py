#conversor de moedas

real = float(input('Quantos reais vc tem? R$'))
dolar = real/4.70
euro = real/5.09
print('Com R${:.2f} reais vc pode comprar ${:.2f} dólares ou €{:.2f} euros'.format(real,dolar,euro))