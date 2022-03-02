n = int(input())
entradas = input()
valores = entradas.split()
a = int(valores[0])
l = int(valores[1])
p = int(valores[2])

if a >= n and l >= n and p >= n:
    print('S')
else:
    print('N')