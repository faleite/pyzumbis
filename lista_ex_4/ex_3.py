""" 3. Faça um programa que crie dois vetores com 10 elementos aleatórios
entre 1 e 100. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois
outros vetores. Imprima os três vetores. """

from random import sample, randint

# Meu código
vetor_1 = sample(range(1, 100), 10)

vetor_2 = sample(range(1, 100), 10)

vetor_3 = []

for index in range(10):
    vetor_3.append(vetor_1[index])
    vetor_3.append(vetor_2[index])

print('Vetor 1:', vetor_1)
print('Vetor 2:', vetor_2)
print('Vetor 3:', vetor_3)

# Com sample, zip e extend
v1 = sample(range(100), 10)
v2 = sample(range(100), 10)
v3 = []
for x in zip(v1, v2):  # zip -> funçao junta mais de um vetor (lembre do ziper)
    v3.extend(list(x))  # extend -> funçao que inseri mais de um intem a lista

print('v1:', v1)
print('v2:', v2)
print('v3:', v3)


# Com randint
v1 = []
v2 = []
v3 = []
for k in range(10):
    x = randint(1, 100)
    v1.append(x)
    v3.append(x)
    x = randint(1, 100)
    v2.append(x)
    v3.append(x)

print('v1:', v1)
print('v2:', v2)
print('v3:', v3)
