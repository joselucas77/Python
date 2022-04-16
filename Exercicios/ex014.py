temperatura = float(input('Informe a temperatura em °C: '))

fahrenheit = temperatura * 1.8 + 32
kelvin = temperatura + 273

print('A temperatura de {:.1f} corresponde a {:.1f}°F e {:.1f}K'.format(temperatura,fahrenheit,kelvin))