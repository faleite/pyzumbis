""" Verificar se uma palavra é palindrome
- Tem o mesmo resultado de tras para frente
- Exemplo: Arara -> ararA
"""

palavra = input('Digite uma palavra: ').lower()

#1 Fórmula
if palavra == palavra[::-1]:
    print(palavra, 'é palindrome')
else:
    print('Não é palindrome')

#2 Fórmula
palindrome = palavra == palavra[::-1]
print(f'{palavra} é palíndrome?')
print(palindrome)
