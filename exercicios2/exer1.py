'''Escreva um programa que compare se duas
 sequências digitadas pelo usuário são iguais.''' 

import re

seq1 = input('Digite a sequencia 1: ')
seq2 = input('Digite a sequencia 2: ')

busca = re.match(seq1,seq2)

if busca:
    print ('sequencias identicas')
    print (busca.group)
else:
    print ('sequencias diferentes')    
