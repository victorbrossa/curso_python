'''Escreva um programa que receba dois números e um sinal, 
e faça a operação matemática definida pelo sinal. '''

num1 = int (input('Digite primeiro numero: '))
operador = input('Digite o operador: ')
num2 = int (input('Digite segundo numero: '))

if operador == '+':
        resultado = num1 + num2
elif operador == '-':
        resultado = num1 - num2
elif operador == '/':
        resultado = num1 / num3
elif operador == '*':
        resultado = num1 * num3

print (resultado)       
