from wsgiref.validate import validator

dias = int(input())
km = int(input())

kmtotal = km / dias

if kmtotal > 100:
    pagar = (kmtotal*12*dias) + 90
    print('%.2f' %pagar)
else :
    pagar = dias*90
    print('%.2f' %pagar)

