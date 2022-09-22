""" Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os
valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
"""
la = int(input('Lado a: '))
lb = int(input('Lado b: '))
lc = int(input('Lado c: '))

if (lb - lc) < la and la < (lb + lc):
    print('É um triângulo')
    if la == lb and lb == lc:
        print('Equilátero')
    elif la == lb or lb == lc or lc == la:
        print('Isóceles')
    elif la != lb and lb != lc:
        print('Escaleno')
else:
    print('Não é um triângulo')
