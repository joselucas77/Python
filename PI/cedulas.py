num = int (input())
ver = num
notas = [0,0,0,0,0,0,0]

while ver != 0:

    if ver >= 100:
        ver -= 100
        notas [6]+= 1
    elif ver >= 50:
        ver -= 50
        notas [5]+= 1    
    elif ver >= 20:
        ver -= 20
        notas [4]+= 1
    elif ver >= 10:
        ver -= 10
        notas [3]+= 1
    elif ver >= 5:
        ver -= 5
        notas [2]+= 1
    elif ver >= 2:
        ver -= 2
        notas [1]+= 1    
    else:
        ver -= 1
        notas [0]+= 1

print ("%d"%num)
print (notas[6],"nota(s) de R$ 100,00")
print (notas[5],"nota(s) de R$ 50,00")
print (notas[4],"nota(s) de R$ 20,00")
print (notas[3],"nota(s) de R$ 10,00")
print (notas[2],"nota(s) de R$ 5,00")
print (notas[1],"nota(s) de R$ 2,00")
print (notas[0],"nota(s) de R$ 1,00")