n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m > 7:
    print('Sua média foi boa, PARABÉNS!')
elif m >= 5 and m <= 7:
    print('Você pode melhorar, estude mais!')
else:
    print('Sua média foi ruim, estude mais!')
