'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = 0
contador = 0
soma = 0
'''ou pode ser feito num = contador = soma = 0'''
num = int(input('Informe um Número ou digite 999 para parar: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Informe um Número ou digite 999 para parar: '))
print(f'Você digitou {contador} números e a soma entre ele foi {soma}')
