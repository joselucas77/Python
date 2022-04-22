n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('=-='*20)
    print('''O que você quer fazer com os números?:
[1]SOMAR
[2]MULTIPLICAR
[3]NOVOS NÚMEROS
[4]MAIOR
[5]SAIR DO PROGRAMA''')
    print('=-='*20)
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        s = n1+n2
        print(f'A soma entre {n1} e {n2} é ugual a {s}')
    elif op == 2:
        m = n1*n2
        print(f'O resultado da multiplicação entre {n1} e {n2} é igual a {m}')
    elif op == 3:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 4:
        if n1 > n2: maior = n1
        else: maior = n2
        print(f'O maior número entre {n1} e {n2} é o {maior}')
    elif op == 5:
        print('Finalizando..')
    else: print('Opção inválida. Tente novamente!')
print('Fim do programa!')