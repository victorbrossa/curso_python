'''Escreva um programa que receba dois números e um sinal, 
e faça a operação matemática definida pelo sinal. '''

nume1 = int (input('Digite primeiro numero: '))
operador = input('Digite o operador: ')
nume2 = int (input('Digite segundo numero: '))

if operador == '+':
        resultado = nume1 + nume2
elif operador == '-':
        resultado = nume1 - nume2
elif operador == '/':
        resultado = nume1 / nume2
elif operador == '*':
        resultado = nume1 * nume2

print (resultado)       
