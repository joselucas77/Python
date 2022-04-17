nome = str(input("Qual o seu nome completo? ")).strip()
print('Analizando seu nome...')
print('''Em maiúsculo fica: {}
Em minúsculo fica: {}
'''.format(nome.upper(), nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
lista = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(lista[0], len(lista[0])))