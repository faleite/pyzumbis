""" REPETIÇÃO
- contadores incremento constante
- acumuladores variável
"""

#  n = int(input('Número: '))

#  x = 0

#  while x <= n:
    #  print(x)
    #  x += 2

n = 1 # Variável Contadora
soma = 0 # Variável Acumuladora

#  while n <= 10:
    #  x = int(input(f'{n} número: '))
    #  soma = soma + x
    #  n = n + 1

#  print(f'Soma: {soma}')
#  print(f'Média: {soma / 10:.1f}')

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
