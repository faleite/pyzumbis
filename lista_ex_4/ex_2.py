""" 2. Sorteie 20 inteiros entre 1 e 100 numa lista.
Armazene os números pares na lista PAR e os números ímpares na lista IMPAR.
Imprima as três listas. """

from random import sample

vetor = sample(range(100), 20)

PAR = []
IMPAR = []

# Meu código
for index in vetor:
    if index % 2 == 0:
        PAR.append(index)
    else:
        IMPAR.append(index)

print('Vetor:', vetor)
print('PAR:', PAR)
print('IMPAR:', IMPAR)


# Com list ccomprehension
par = [x for x in vetor if x % 2 == 0]
ímpar = [x for x in vetor if x % 2 == 1]

print('Vetor', vetor)
print('Pares', par)
print('Ímpares', ímpar)
