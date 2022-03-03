entrada = input()
valores = entrada.split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

def omaior(a, b, c):
    maiorAB = (a + b + abs(a-b)) / 2
    
    if maiorAB < c:
        return(c)
    elif maiorAB > a:
        return(b)
    elif maiorAB > b:
        return(a)

res = omaior(a, b, c)
print('%i eh o maior' %res)