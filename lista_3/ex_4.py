""" A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então,
cada elemento é a soma dos dois anteriores.
Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci.
F1 = 1, F2 = 1, F3 = 2, etc.
"""
# Uso de atribuição múltipla

n = int(input('Número inteiro: '))
a, b = 1, 1
#  seq = [a, b]

for i in range(n-2):
    a, b = b, a + b
    #  seq.append(b)
print(f'F{n} = {b}')
#  print(seq)
