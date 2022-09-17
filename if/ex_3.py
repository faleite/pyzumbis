""" Exercício com o condicional 'if' """

velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 110:
    print('Você foi multado!')
    multa = (velocidade - 110) * 5
    print(f'Valor da multa: R$ {multa:.2f}')
else: # Caso contrário - se não
    print('Siga em frente!')
