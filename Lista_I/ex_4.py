""" Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário. """

salario = float(input('Sálario: '))
porcentagem = float(input('Aumento %: '))
aumento = salario * porcentagem / 100
novo_salario = salario + aumento
print(f'Aumento: {aumento:.2f}€\nNovo salário: {novo_salario:.2f}€')
