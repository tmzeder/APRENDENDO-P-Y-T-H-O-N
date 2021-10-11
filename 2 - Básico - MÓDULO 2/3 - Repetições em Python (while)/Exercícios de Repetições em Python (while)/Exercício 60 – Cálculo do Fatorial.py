'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''


'''COM BIBLIOTECA:

from math import factorial

num =  int(input('Informe o nº que deseja saber o fatorial: '))
f = factorial(num)
print(f'O fatorial de {num} é: {f}')'''

# Tradicional:

num =  int(input('Informe o nº que deseja saber o fatorial: '))
contador = num
fat = 1 # qualquer coisa multiplicado por 1 é igual a ela mesma
print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(f'{contador}', end =' ' )
    print(' x ' if contador >1 else ' = ', end= '')
    fat *= contador
    contador -= 1
print(f'O fatorial de {num} é: {fat}')