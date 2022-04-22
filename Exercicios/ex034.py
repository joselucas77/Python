salario = float(input('Qual o valor do seu salário? R$'))
if salario <= 1250: 
    novoSalario = (0.15*salario) + salario
    print(f'Seu novo salário passa a ser R${novoSalario:.2f}')
else:
    novoSalario = (0.10*salario) + salario
    print(f'Seu novo salário passa a ser R${novoSalario:.2f}')