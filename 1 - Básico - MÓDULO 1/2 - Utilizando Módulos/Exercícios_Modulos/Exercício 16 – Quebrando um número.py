#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

num = float(input('Digite un número: '))
print(f'A porção inteira de {num} é = {trunc(num)}')