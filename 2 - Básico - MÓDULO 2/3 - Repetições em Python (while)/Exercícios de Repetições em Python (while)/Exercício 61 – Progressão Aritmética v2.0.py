'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('Gerador de PA ')
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Informe a Razão da PA: '))
termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} →', end=' ')
    termo += razão
    contador += 1
print('FIM')
