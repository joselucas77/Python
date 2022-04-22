from ast import Num
from random import randint
from time import sleep
computador = randint(0,10)
print('-=-'*20)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
print('-=-'*20)
acertou = False
palpites = 0
while not acertou:
    num = int(input('Qual o seu palpite: '))
    print('PROCESSANDO...')
    sleep(2)
    palpites += 1
    if num == computador:
        acertou = True
    else:
        if num < computador:
            print('Mais... Tente mais uma vez: ')
        elif num > computador:
            print('Menos... Tente mais uma vez: ')
print(f'Parabéns! Você acertou com {palpites} tentativas.')
