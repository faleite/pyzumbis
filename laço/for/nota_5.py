""" REPETIÇÃO COM O 'FOR'
- for é um while mais podereso
- Vê elemento do contador e condições de parada automagicamente
- Na maior parte das vezes utilizamos o for
"""

# Uso do for
for i in range(5):
    print(i)

print()

# Mesmo código com uso do while
lista = list(range(5))
k= 0
while k < len(lista):
    i = lista[k]
    print(i)
    k += 1
