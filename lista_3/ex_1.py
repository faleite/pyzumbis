""" Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido. """

nota = int(input('Nota entre zero e dez: '))

while nota > 10 or nota < 0:
    print('Valor inválido')
    nota = int(input('Tente novamente: '))
else:
    print(f'{nota} é uma nota válida')
