""" Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.
"""
# Algoritimo de Euclides:
#  a  b <-> a % b
# 21 15       6
# 15  6       3
#  6  3       0
# a, b = b, a % b

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

while a % b != 0:
    a, b = b, a % b
print(f'mdc = {b}')
