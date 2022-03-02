salario = (float(input()))
aumento = float(input())
porcentagem = salario * (aumento/100)
novoSalario = salario + porcentagem
print('Seu salario teve aumento de {} %, passando de R$ {} para R$ {}'.format(aumento,salario,novoSalario))