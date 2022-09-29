""" Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome
do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

nome = input('Seu nome: ')
senha = input('Senha: ')

#  while senha == nome:
    #  print('Error: A senha não pode ser igual ao nome!')
    #  print('Tente novamente!')
    #  nome = input('Seu nome: ')
    #  senha = input('Senha: ')

while True:
    if senha == nome:
        print('Error: A senha não pode ser igual ao nome!')
        print('Tente novamente!')
        nome = input('Seu nome: ')
        senha = input('Senha: ')
    else:
        break
