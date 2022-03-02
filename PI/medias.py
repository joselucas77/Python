tMedia = input()
a = int(input())
b = int(input())
c = int(input())

if tMedia == 'A':
    media = (a+b+c)/3
elif tMedia =='H':
    media = 3/((1/a)+(1/b)+(1/c))
elif tMedia == 'G':
    media = (a*b*c)**(1/3)

print('%.3f'%media)