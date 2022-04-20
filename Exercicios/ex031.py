dis = float(input('Qual é a distância de sua viagem? '))
print(f'Você esta preste a começar uma viagem de {dis}Km')
preco = dis*0.50 if dis <= 200 else dis*0.45
print('E o preço de sua viagem é de R${:.2f}'.format(preco))