""" Escreva um programa que leia um valor em metros e o exiba convertido em milímetros """

valor_m = float(input('Digite um valor e metros: '))

mm = valor_m * 1000

print(f'{valor_m:.2f} m, é igual a {mm:.2f} mm)')

# Outra forma:
print(f'Milimetros: {valor_m * 1000:.0f}')
