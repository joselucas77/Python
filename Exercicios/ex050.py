num = input('Informe seis números: ').split()
a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])
e = int(num[4])
f = int(num[5])
s = 0

for c in range(a, f+1):
    if c % 2 == 0:
        s += c
print(s)
