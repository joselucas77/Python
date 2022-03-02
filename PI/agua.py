entrada = input()
valores = entrada.split()
m3 = float(valores[0])
custo = float(valores[1])
agua = m3 * 1000
va = (m3 * custo) * 1000
ve = 0.8 * va
vt = va + ve
print('%.2f\n%.2f\n%.2f' %(va,ve,vt))