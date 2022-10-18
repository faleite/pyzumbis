""" 2. Sorteie 20 inteiros entre 1 e 100 numa lista.
Armazene os números pares na lista PAR e os números ímpares na lista IMPAR.
Imprima as três listas. """

import random

sort_20_int = random.sample(range(100), 20)

PAR = []
IMPAR = []

for index in sort_20_int:
    if index % 2 == 0:
        PAR.append(index)
    else:
        IMPAR.append(index)

print('PAR:', PAR)
print('IMPAR:', IMPAR)
