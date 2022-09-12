""" Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. """

qtd_km = float(input('Quantidade de Km: '))
qtd_dias = int(input('Quantidade de dias: '))

custo = (60 * qtd_dias) + (0.15 * qtd_km)

print(f'Preço a pagar: R$ {custo:.2f}')
