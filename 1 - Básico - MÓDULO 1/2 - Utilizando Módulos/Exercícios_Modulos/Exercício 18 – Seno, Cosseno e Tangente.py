#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

a = float(input('Angulo de: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print(f'Valor do Seno:{seno:.2f}\n Valor do Cosseno: {cosseno:.2f}\n Valor da Tangente: {tangente:.2f}')
#nos exemplos tive que transaformar o valor de seno, cosseno e tangente em radianos ultilizando a função math.radians