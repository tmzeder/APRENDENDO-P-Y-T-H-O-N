#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for c in range (1, 8):
    nasc = int(input(f'Informe o Ano de Nascimento da {c}ª Pessoa: '))
    idade = atual - nasc
    if idade >= 18:
       totalmaior +=1
    else:
        totalmenor +=1
print(f'Existem ao todo {totalmaior} pessoas Maiores de Idade e {totalmenor} Menores de Idade.')
   
    

          