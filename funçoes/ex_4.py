""" FUNÇÕES

- random e funções aleatórias

"""

import random  # Importa a função random

dir(random)  # lista todas as funções posiveis do 'random'

# A função 'random.randit(a, b)'retorna um número inteiro aleatório entre dois parâmetros
#  help(random.randint)
""" Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
"""

# Retorna um número inteiro aleatório entre dois parâmetros
print(random.randint(1, 100))

# função '.split()' retona uma lista. Por default usa o espaço para pegar os intens
nomes = 'ze lia pedro luiz'.split()
#  >>> nomes
#  ['ze', 'lia', 'pedro', 'luiz']

# A função 'random.choice()' pega um item aleatório da lista
#  >>> random.choice(nomes)
#  'ze'
#  >>> random.choice(nomes)
#  'luiz'

# A função 'random.shuffle()' mistura a lista
#  >>> random.shuffle(nomes)
#  >>> nomes
#  ['pedro', 'ze', 'lia', 'luiz']

# A função 'random.sample()' retorna uma sequência de números aleatório de uma lista
#  >>> random.sample(range(100), 10) #  retorna 10 números aleatórios entre 0 a 99
#  [90, 63, 46, 4, 26, 85, 0, 55, 93, 83]
