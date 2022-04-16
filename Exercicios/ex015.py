qtd_km = float(input('Quantos KM vc percorreu? '))
qtd_dias = int(input("Quantos dias vc passou com o carro? "))

custo = 60*qtd_dias + 0.15*qtd_km

print('O valor total a ser pago é de R${:.2f}'.format(custo))