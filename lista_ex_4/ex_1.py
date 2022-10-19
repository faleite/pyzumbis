""" 1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior
e o menor valor, sem usar as funções max e min. """

from random import sample

vetor = sample(range(100), 10)

menor = maior = vetor[0]

# Meu código
#  for index in vetor:
    #  if index < menor:
        #  menor = index
    #  if index > maior:
        #  maior = index

#  print('Vetor:', vetor)
#  print('Maior valor:', maior)
#  print('Menor valor:', menor)

# Código com o while
#  k = 1
#  while k < 10:
    #  if vetor[k] > maior: maior = vetor[k]
    #  if vetor[k] < menor: menor = vetor[k]
    #  k = k + 1

# Código com o for
for x in vetor[1:]:
    if x > maior: maior = x
    if x < menor: menor = x

print('Vetor:', vetor)
print(f'Maior: {maior}')
print(f'Menor: {menor}')
