""" Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário. """

salario = float(input('Sálario: '))
aumento = float(input('Aumento: '))

novo_salario = (salario * aumento / 100) + salario
print(f'{novo_salario:.2f}')
