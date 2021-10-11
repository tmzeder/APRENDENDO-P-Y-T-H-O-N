#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Informe um número: '))
total = 0

for c in range (1, num  + 1): # pois o python conta sempre um a menos por isso o +1
    if num % c == 0:
        print('\033[33m', end=' ') # Amarelo indica os valores que o nº é divisivel.
        total += 1
    else:
        print('\033[31m', end=' ') # Vermelho indica os valores que o nº não é divisivel.
    print(f'{c}', end=' ')
print(f'\n\033[m O numero {num} foi divisivél {total} vezes')
if total == 2:
    print('Por isso ele É PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO.')
print('FIM DO PROGRAMA.')
