'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = 'S'
menor = maior = quanti = media = soma = 0

while resposta in 'Ss':
    num = int(input('Informe um valor: '))
    soma += num
    quanti += 1
    if quanti == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? S/N ')).upper().strip()[0]
media = soma / quanti
print(f'Você digitou {quanti} números, e a media entre eles foi: {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
    