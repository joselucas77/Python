from math import hypot
co = float(input('Qual o comprimento do cateto oposto do triângulo? '))
ca = float(input('Qual o comprimento do cateto adjacente do triângulo? '))
hi = hypot(co,ca)
print('A Hipotenusa vai medir {:.2f}'.format(hi))