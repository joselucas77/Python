num = int(input())
res = num % 10

if num < 0:
    res = -num % 10
    print("-%i" %res)
else :
    print('%i' %res)