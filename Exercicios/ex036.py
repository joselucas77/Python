casa = float(input('Qual o valor da casa a ser financiada? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos vc quer pagar a casa? '))
prestacao = casa/anos
if prestacao > 0.30*salario:
    print('Infelizmente você não pode fazer o financiamento, pois sua renda não é o suficiente.')
else: print('O financiamneto foi aceito, sua prestação mensal será de R${prestacao:.2f}') 
