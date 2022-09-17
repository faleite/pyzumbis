""" Verificar se um carro é novo ou velho """

# Se o carro tiver pelo menos três anos é novo
idade = int(input('Digite a idade de seu carro: '))
if idade <= 3:
    print('Seu carro é novo')
else: # (if idade > 3:) Quando a há duas condições complementares, pode-se usar o "else"
    print('Seu carro é velho')
