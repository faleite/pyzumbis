""" REPETIÇÃO COM O 'FOR'
- for é um while mais podereso
- Vê elemento do contador e condições de parada automagicamente
- Na maior parte das vezes utilizamos o for
"""

# Uso do for
for i in ['cpbr6', 42, 3.14]:
    print(i)

print()

# Mesmo código com uso do while
lista = ['cpbr6', 42, 3.14]
k = 0
while k < len(lista):
    i = lista[k]
    print(i)
    k += 1
