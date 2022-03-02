n1 = int(input())
n2 = int(input())
n3 = int(input())

menor = n1

if menor > n2:
    menor = n2
if menor > n3:
    menor = n3

print(menor)