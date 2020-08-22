'''Escreva um programa que resolva uma equação de segundo grau.'''
from math import sqrt

a = int (input('Digite o valor de a: '))
b = int (input('Digite o valor de b: '))
c = int (input('Digite o valor de c: '))

print(type(b))

delta = float( b**2 - 4*a*c)
print(delta)
raiz_delta = sqrt(delta) 

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print ("x1 = %f" %x1)
print ("x2 = %f" %x2)
