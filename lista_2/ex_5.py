""" Faça um Programa que leia três números e mostre o maior deles. """

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

# fórmula 1
if n1 > n2 and n1 > n3:
    print(f'Maior número: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'Maior número: {n2}')
else:
    print(f'Maior número: {n3}')

if n1 < n2 and n1 < n3:
    print(f'Menor número: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'Menor número: {n2}')
else:
    print(f'Menor número: {n3}')

# fórmula 2
print('\nMaior número:', max([n1, n2, n3]))
print('Menor número:', min([n1, n2, n3]))
