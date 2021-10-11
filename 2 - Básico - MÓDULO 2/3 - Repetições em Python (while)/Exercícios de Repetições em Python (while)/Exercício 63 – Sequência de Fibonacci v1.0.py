'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8''' #a sequencia de Fibonacci começa sempre com 0 e 1 trata-se da soma de zero mais 1 depois 1 + 1, 1 + 2 = 3, 3 + 2 = 5 e assim Sucessivamente.


print('-*-'* 30)
print('Sequência de Fibonacci ')
num = int(input(' Informe quantos números você quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end=' ')
contador = 3
while contador <= num:
    t3 = t1 + t2
    print(f'→ {t3}', end=' ')
    t1 = t2
    t2 = t3
    contador += 1
print('FIM')
