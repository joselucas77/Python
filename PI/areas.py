import math

entrada = input()
valores = entrada.split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
pi = 3.14159
tri = (a*c)/2
cir = pi*(c**2)
tra = ((a+b)/2)*c
qua = b*b
ret = a*b
print('TRIANGULO: %.3f' %tri)
print('CIRCULO: %.3f' %cir)
print('TRAPEZIO: %.3f' %tra)
print('QUADRADO: %.3f' %qua)
print('RETANGULO: %.3f' %ret)