""" REPETIÇÃO COM O 'FOR'
- for é um while mais podereso
- Vê elemento do contador e condições de parada automagicamente
- Na maior parte das vezes utilizamos o for
"""

# Uso do for
for i in 'aeiou':
    print(i)

print()

# Mesmo código com uso do while
texto = 'aeiou'
k = 0
while k < len(texto):
    i = texto[k]
    print(i)
    k += 1
