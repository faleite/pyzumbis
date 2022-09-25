""" REPETIÇÃO
- while dentro de while
"""
# Code que mostra 10 tabuadas (1 ao 10)
t = 1
while t <= 10:
    print(f'Tabuada do {t}')
    n = 1
    while n <= 10:
        print(f'{t} x {n} = {t*n}')
        n = n + 1
    t = t + 1
    print()
