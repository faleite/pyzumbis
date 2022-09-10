#TWP050
resposta = 42
print('Resposta para tudo é:', resposta)

print(f'tudo tem {resposta} como solução')

preço = 9.6666

print(f'Preço é € {preço:.2f}')

# int com str não concatena
#  In [1]: 42 + 'abacates'
#  ---------------------------------------------------------------------------
#  TypeError                                 Traceback (most recent call last)
#  Input In [1], in <cell line: 1>()
#  ----> 1 42 + 'abacates'
# É preciso tratar o int para str
#  In [3]: str(42) + ' abacates'
#  Out[3]: '42 abacates'

# Os dados tem métodos:
# Use o . + TAB para ver lista de métodos
'abacate'.upper() # uppercase -> ABACATE

# Troca de valores:
#  In [6]: a = 3
#  In [7]: b = 'abacate'
#  In [8]: a, b = b, a
#  In [9]: a
#  Out[9]: 'abacate'
#  In [10]: b
#  Out[10]: 3

# Atribuição de valores
#  In [11]: a, b, c = 1, 2, 3
#  In [12]: d, m , a = '21/03/2020'.split('/')
#  In [13]: d
#  Out[13]: '21'
#  In [14]: m
#  Out[14]: '03'
#  In [15]: a
#  Out[15]: '2020'


