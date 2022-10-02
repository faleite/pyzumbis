"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê
o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que
Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido,
conforme a tabela abaixo:

a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato (5%) : R$
e. = Salário Liquido : R$
"""

vh = float(input('Valor hora: '))
htm = int(input('Horas trabalhadas: '))
sb = vh * htm

print(f'+ Salário Bruto:\t R$ {sb:.2f}')
print(f'- IR (11%):\t\t R$ {sb * 0.11:.2f}')
print(f'- INSS (8%):\t\t R$ {sb * 0.08:.2f}')
print(f'- Sindicato (5%):\t R$ {sb * 0.05:.2f}')
print(f'= Salário Liquido:\t R$ {sb - (sb * 0.24):.2f}')
