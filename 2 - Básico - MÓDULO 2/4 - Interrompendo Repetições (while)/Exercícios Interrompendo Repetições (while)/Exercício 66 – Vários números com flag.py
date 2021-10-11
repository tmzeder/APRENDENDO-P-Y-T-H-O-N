'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

num = soma = contador = 0

while True:
    num = int(input('Informe um número ou Digite 999 para encerrar o programa: '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'A Soma dos valores é: {soma}.\nForam digitados {contador} valores.')