salario = float(input('Qual o valor do seu salário? R$'))
if salario <= 1250: 
    novoSalario = (0.15*salario) + salario
    print('Seu novo salário passa a ser R${:.2f}'.format(novoSalario))
else:
    novoSalario = (0.10*salario) + salario
    print('Seu novo salário passa a ser R${:.2f}'.format(novoSalario))