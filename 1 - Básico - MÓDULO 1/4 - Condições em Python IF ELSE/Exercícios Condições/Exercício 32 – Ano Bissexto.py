#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.



ano = int(input('Informe o Ano que deseja analisar! '))
if ano %4 == 0 and ano %100 !=0 or ano %400 == 0: #Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).
    print(f'O Ano de {ano} É BISSEXTO ')
else: print(f'o Ano de {ano} NÃO é BISEEXTO')


#outra forma de fazer usando o import date:
from datetime import date

ano = int(input('Informe o ano ou digite 0 para o ano Atual: '))
if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano %100 !=0 or ano %400 == 0:
    print(f'O ano de {ano} É BISSEXTO!')
else: print(f'O Ano de {ano} NÃO é BISEEXTO!')   