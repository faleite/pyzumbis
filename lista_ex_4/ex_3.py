""" 3. Faça um programa que crie dois vetores com 10 elementos aleatórios
entre 1 e 100. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois
outros vetores. Imprima os três vetores. """

import random

vetor_1 = random.sample(range(1, 100), 10)

vetor_2 = random.sample(range(1, 100), 10)

vetor_3 = []

for index in range(10):
    vetor_3.append(vetor_1[index])
    vetor_3.append(vetor_2[index])

print('Vetor 1:', vetor_1)
print('Vetor 2:', vetor_2)
print('Vetor 3:', vetor_3)

