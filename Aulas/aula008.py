from math import sqrt, floor
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))