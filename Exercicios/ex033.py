num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
menor = num1
maior = num1
if num2 < num1 and num2 < num3: menor = num2
elif num3 < num1 and num3 < num2: menor = num3
if num2 > num1 and num2 > num3: maior = num2
elif num3 > num1 and num3 > num2: maior = num3
print(f'''O maior valor digitado foi o {maior}
E o menor valor digitado foi o {menor}''')