''' Faça um programa que receba a idade
do usuario e diga se ele eh maior ou menor de idade'''

nome = input ('Digite seu nome: ')
idade = int (input('Digite sua idade: '))
print(nome)
print(idade)
if idade >= 18:
    print('eh maior de idade')
else:
    print('eh menor de idade')
