V0 = float(input())
A = float(input())
T = float(input())

def velkmh(V0, A, T):
    V = V0 + (A*T)
    return(V * 3.6)


maior = velkmh(V0, A, T)
velkmh(V0, A, T) == 0

V0 = float(input())
A = float(input())
T = float(input())

def velkmh(V0, A, T):
    V = V0 + (A*T)
    return(V * 3.6)


meio = velkmh(V0, A, T)
velkmh(V0, A, T) == 0


V0 = float(input())
A = float(input())
T = float(input())

def velkmh(V0, A, T):
    V = V0 + (A*T)
    return(V * 3.6)


menor = velkmh(V0, A, T)
velkmh(V0, A, T) == 0


def MENOR(maior, meio, menor):
    if maior < meio and maior < menor:
        return(maior)
    elif meio < maior and meio < menor:
        return(meio)
    elif menor < maior and menor < meio:
        return(menor)

res = MENOR(maior, meio, menor)
print('%.1f' %res)