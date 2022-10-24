""" Google Developer Day 2010

Questão C. Entre 1067 e 3627 (inclusive),
quantos números são pares e também divisíveis por 7?

Resposta: 183

"""

lista = []
lista2 = []

for index in range(1067, 3628):
    if index % 2 == 0:
        lista.append(index)

for index in lista:
    if index % 7 == 0:
        lista2.append(index)

print(len(lista2))
