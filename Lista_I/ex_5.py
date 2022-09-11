""" Solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar. """

preco = float(input('Preço da mercadoria: '))
desconto = float(input('Percentual de desconto: '))

valor_desconto = preco * desconto / 100
pagar = preco - valor_desconto

print(f'Valor do desconto: € {valor_desconto:.2f}')
print(f'Preço a pagar: € {pagar:.2f}')
