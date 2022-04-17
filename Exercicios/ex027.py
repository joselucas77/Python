n = str(input('Digite seu nome? ')).strip()
nome = n.split()
print(f'Muito prazer em te conhecer {nome[0]}!')
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))