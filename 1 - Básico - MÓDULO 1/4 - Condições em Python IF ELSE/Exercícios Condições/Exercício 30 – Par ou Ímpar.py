#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Iforme um número: '))
res = num % 2 #resto da divisão por 2, para pares sobra 0 e para impares sobra 1!!!

if res == 0:
    print(f'O {num} é PAR! ')
else:
    print(f'O {num} é IMPAR')

print('FIM DO PROGRAMA...')    