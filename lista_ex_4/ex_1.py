""" 1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior
e o menor valor, sem usar as funções max e min. """

import random

sorteio_10_int = random.sample(range(1, 101), 10)

print(sorteio_10_int)

menor, maior = sorteio_10_int[0], sorteio_10_int[0]

for index in sorteio_10_int:
    if index < menor:
        menor = index
    if index > maior:
        maior = index

print('Maior valor:', maior)
print('Menor valor:', menor)

