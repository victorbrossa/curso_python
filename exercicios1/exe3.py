'''Escreva um programa que resolva uma equação de segundo grau.'''

from math import sqrt

a = int (input('Digite o valor de a: '))
b = int (input('Digite o valor de b: '))
c = int (input('Digite o valor de c: '))


d = float( b**2 - 4*a*c)
print('delta: ', d)

if d > 0:
    delta = sqrt(d)
    print('Raiz quadrada de delta: ', delta)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print('x1 = ', x1, 'x2 = ', x2)

elif d == 0:
    delta = sqrt(d)
    print('Raiz quadrada de delta: ', delta)
    x = -b / (2 * a)
    print ('valor de x = ', x)

elif d < 0:
    print('Essa raiz eh menor do que zero')
