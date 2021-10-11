'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

mais18 = 0
homens = 0
mulhermenos20 = 0

while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        mulhermenos20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total de pessoas com 18 anos é de: {mais18}\nO total Homens cadastrados é de: {homens}\nQuantidade de mulheres com menos de 20 anos: {mulhermenos20}')        
