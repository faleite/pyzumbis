""" REPETIÇÃO COM O 'WHILE'
- contadores incremento constante
- acumuladores variável
"""

# acumulador pode ser de produto
# fatorial de 10
#  1 * 2 * 3 * ...* 9 * 10

k = 1 # Contador
fat = 1 # Acumulador (sempre deve começar com um elemento neútro, no caso o múmero 1)
n = int(input('número: '))

while k <= n:
    fat = fat * k
    k = k + 1

print(f'fat({n}) = {fat}')
