# Manipulando Texto 

frase = 'Curso em Video Python'
# [c,u,r,s,o, ,e,m, ,v, i, d, e, o,  , p, y, t, h, o, h]
# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Fatiamento
# [a:b:c]=> a é onde começa; b é até onde para; c é pulando de c em c
print(frase[9])
# retorna 'v'
print(frase[9:13])
# retorna 'vide'
print(frase[9:21:2])
# retorna 'vdopto'
print(frase[:5])
# retorna 'curso'
print(frase[15:])
# retorna 'python'

# Análize
# mostra a quantidade de caracteres(contando tbm os espaços)
print(len(frase))
# faz a contagem dos caracteres desejados no ()
print(frase.count('o',0,13))
# retorna 1
# mostra onde comecou o parâmetro desejados no  ()
# se vc receber como resultado -1, é pq o parâmetro/string não existe
print(frase.find('deo'))
# retorna 11
# cerifica se a string existe na frase (true or false)
print('curso' in frase)
# retorna True

# Transformação
# substitue uma string da frase por outra desejada, porém não modifica a lista 'geral'
print(frase.replace('python','android'))
# coloca tudo em maiúsculo
print(frase.upper())
# coloca tudo em minúsculo
print(frase.lower())
# coloca tudo em minúsculo, porém a primeira string fica em maiúscula
print(frase.capitalize())
# coloca toda primeira string de uma palavra em maiúscula
print(frase.title())
frase = '   Aprenda Python  '
# tira espaços desnecessários do texto
print(frase.strip())

# Divisão
frase = 'Curso em Video Python'
# faz uma divisão das strings considerando os espaços
print(frase.split())

# Junção
print('-'.join(frase))
