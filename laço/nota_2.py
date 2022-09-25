""" REPETIÇÃO
- contadores incremento constante
- acumuladores variável
"""

n = 1 # Variável Contadora
soma = 0 # Variável Acumuladora

while n <= 10:
    x = int(input(f'{n} número: '))
    soma = soma + x
    n = n + 1

print(f'Soma: {soma}')
print(f'Média: {soma / 10:.1f}')
