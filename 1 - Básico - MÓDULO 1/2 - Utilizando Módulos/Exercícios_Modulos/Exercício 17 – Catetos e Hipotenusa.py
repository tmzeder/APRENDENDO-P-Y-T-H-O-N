#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. "hip ao quadrado = soma do quadrado dos catetos"

#maneira matemática de resolver:

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: ')) 
hip = (co**2 + ca**2) **(1/2) # esse **1/2 é a maneira de fazer elevado a raiz quadrada

print(f'O comprimento da hipotenusa é de:{hip:.2f}')


#maneira com importação de biblioteca:

import math
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = math.hypot(co, ca)

print(f'O comprimento da hipotenusa é: {hi:.2f}')

