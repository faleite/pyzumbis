""" Converta uma temperatura digitada em Fahrenheit para Celsius. """

f = float(input('Fahrenheit: '))

print(f'Celsius: {(f - 32) / 1.80:.1f}')

# Outra Fórmula:
print(f'Celsius: {(f - 32) * 5 / 9:.1f}')
