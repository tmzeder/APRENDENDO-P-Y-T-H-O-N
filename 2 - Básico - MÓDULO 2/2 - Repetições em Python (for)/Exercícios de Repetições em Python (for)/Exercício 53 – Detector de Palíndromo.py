#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma Frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for c in range (len(junto) - 1, -1, -1):
    inverso += junto[c]
print(f'o inverso de {inverso} é {junto}.')
if inverso == junto:
    print('Temos um palindromo.')
else:
    print('A frase digitada não é um palindromo.')
