'''Faça um programa que receba duas notas digitadas pelo usuário.
Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.'''

nome = input('Digite seu Nome: ')
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
media = int

media = (nota1 + nota2) / 2

if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')    