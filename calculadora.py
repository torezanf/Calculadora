#!/bin/bash

#Solicita ao usuario qual operação matemática a ser realizada
opMat = input('''Qual operação matemática gostaria de realizar?
Adição
Subtração
Multiplicação
Divisão
''')
#Solicita o primeiro numero da equação
num1 = int(input('Digite o primeiro número:'))

#Solicita o segundo numero da equação
num2 = int(input('Digite o segundo número:'))

#Compara a opeação selecionada e realiza a conta matemática
if opMat == 'Adição':
    print('O valor da sua soma é:',num1 + num2)
elif opMat == 'Subtração':
    print('O valor da sua subtração é:' ,num1 - num2)

elif opMat == 'Multiplicação':
    print('O valor da sua multiplicação é:' ,num1 * num2)

elif opMat == 'Divisão':
    print('O valor da sua divisão é:' ,num1 / num2)

else:
    print('Operação inválida')

