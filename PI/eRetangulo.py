a = int(input())
b = int(input())
c = int(input())
d = int(input())

def eRetangulo(a, b, c, d):
    if a == b and c == d or a == c and b == d or a == d and c == b:
        return('RETANGULO')
    else :
        return('NAO EH UM RETANGULO')


print(eRetangulo(a, b, c, d))