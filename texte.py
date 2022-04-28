num = int(input('Digite um numero: '))
op = False
while not op:
    if num == 0 or num == 1:
        print(f'Fatorial de {num} é 1.')
        break
    elif num != 0 and num > 1:
        fatorial = num * (num-1)
        print(f'O fatorial de {num} é {fatorial}')
        break
    else:
        print('Número inválido!')
        num = int(input('Digite um numero: '))
        continue
res = str(input('Quer ler outro numero?(S/N) '))
if res == 'S':
    num = int(input('Digite um numero: '))
    while not op:
        if num == 0 or num == 1:
            print(f'Fatorial de {num} é 1.')
            break
        elif num != 0 and num > 1:
            fatorial = num * (num-1)
            print(f'O fatorial de {num} é {fatorial}')
            break
        else:
            print('Número inválido!')
            num = int(input('Digite um numero: '))
            continue
else:
    print('Fim do programa!')