print('-=' * 20)
num = int(input('''Informe uma das opções abaixo:
[1]- Soma.
[2]- Subtrair.
[3]- Multiplicar.
[4]- Dividir.
[5]- Bhaskara.
[6]- Sair do programa.
: '''))
print('-=' * 20)


def continuarPrograma(a):
    return '''Informe uma das opções abaixo:
[1]- Soma.
[2]- Subtrair.
[3]- Multiplicar.
[4]- Dividir.
[5]- Bhaskara.
[6]- Sair do programa.
: '''


def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + (delta ** 1 / 2)) / 2 * a
    x2 = (-b - (delta ** 1 / 2)) / 2 * a
    res = print(f"As raízes da esquação são {x1} e {x2}")
    return res


op = False
while not op:
    if num == 1:
        a = float(input('Informe um número: '))
        b = float(input('Digite outro número: '))
        soma(a, b)
        print(f'A soma entre {a:.2f} e {b:.2f} é {soma(a, b):.2f}')
        res = input('Deseja fazer esta mesma operação com novos números? (S/N) ').upper()
        if res == 'S':
            continue
        elif res == 'N':
            res2 = input('Degeja fazer outro tipo de operação? (S/N )').upper()
            if res2 == 'S':
                num = input(continuarPrograma(a))
            else:
                break
        else:
            print('Programa encerrado!')
            break
    elif num == 2:
        a = float(input('Informe um número: '))
        b = float(input('Digite outro número: '))
        subtrair(a, b)
        print(f'A subtração entre {a:.2f} e {b:.2f} é {subtrair(a, b):.2f}')
        res = input('Deseja fazer esta mesma operação com novos números? (S/N) ').upper()
        if res == 'S':
            continue
        elif res == 'N':
            res2 = input('Degeja fazer outro tipo de operação? (S/N )').upper()
            if res2 == 'S':
                print('-=' * 20)
                num = int(input('''Informe uma das opções abaixo:
[1]- Soma.
[2]- Subtrair.
[3]- Multiplicar.
[4]- Dividir.
[5]- Bhaskara.
[6]- Sair do programa.
: '''))
                print('-=' * 20)
            else:
                break
        else:
            print('Programa encerrado!')
            break
    elif num == 3:
        a = float(input('Informe um número: '))
        b = float(input('Digite outro número: '))
        multiplicar(a, b)
        print(f'A multiplicação entre {a:.2f} e {b:.2f} é {multiplicar(a, b):.2f}')
        res = input('Deseja fazer esta mesma operação com novos números? (S/N) ').upper()
        if res == 'S':
            continue
        elif res == 'N':
            res2 = input('Degeja fazer outro tipo de operação? (S/N )').upper()
            if res2 == 'S':
                print('-=' * 20)
                num = int(input('''Informe uma das opções abaixo:
[1]- Soma.
[2]- Subtrair.
[3]- Multiplicar.
[4]- Dividir.
[5]- Bhaskara.
[6]- Sair do programa.
: '''))
                print('-=' * 20)
            else:
                break
        else:
            print('Programa encerrado!')
            break
    elif num == 4:
        a = float(input('Informe um número: '))
        b = float(input('Digite outro número: '))
        dividir(a, b)
        print(f'A divisão entre {a:.2f} e {b:.2f} é {dividir(a, b):.2f}')
        res = input('Deseja fazer esta mesma operação com novos números? (S/N) ').upper()
        if res == 'S':
            continue
        elif res == 'N':
            res2 = input('Degeja fazer outro tipo de operação? (S/N )').upper()
            if res2 == 'S':
                print('-=' * 20)
                num = int(input('''Informe uma das opções abaixo:
[1]- Soma.
[2]- Subtrair.
[3]- Multiplicar.
[4]- Dividir.
[5]- Bhaskara.
[6]- Sair do programa.
: '''))
                print('-=' * 20)
            else:
                break
        else:
            print('Programa encerrado!')
            break
    elif num == 5:
        a = float(input('Informe um número: '))
        b = float(input('Digite outro número: '))
        c = float(input('Digite outro número: '))
        bhaskara(a, b, c)
        print(f'{bhaskara(a, b, c)}')
        res = input('Deseja fazer esta mesma operação com novos números? (S/N) ').upper()
        if res == 'S':
            continue
        elif res == 'N':
            res2 = input('Degeja fazer outro tipo de operação? (S/N )').upper()
            if res2 == 'S':
                print('-=' * 20)
                num = int(input('''Informe uma das opções abaixo:
[1]- Soma.
[2]- Subtrair.
[3]- Multiplicar.
[4]- Dividir.
[5]- Bhaskara.
[6]- Sair do programa.
: '''))
                print('-=' * 20)
            else:
                break
        else:
            print('Programa encerrado!')
            break
    elif num == 6:
        print('Programa encerrado!')
        break
    else:
        print('-=' * 20)
        print('Opção inválida!')
        print('-=' * 20)
        num = int(input('''Informe uma das opções abaixo:
[1]- Soma.
[2]- Subtrair.
[3]- Multiplicar.
[4]- Dividir.
[5]- Bhaskara.
[6]- Sair do programa.
: '''))
        print('-=' * 20)