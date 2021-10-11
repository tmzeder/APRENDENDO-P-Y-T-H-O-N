'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

total_gasto = 0
mais_de_mil = 0
nome_barato = ' '
quantidade_produto = 0
valor_barato = 0
# Poderia ser feito: total_gasto = mais_de_mil = quantidade_produto = valor_barato = 0 que funciona da mesma maneira.

while True:
    nome_produto = str(input('Informe o nome do produto: '))
    preco_produto = float(input('Informe o preço do produto: R$'))
    total_gasto += preco_produto
    quantidade_produto += 1
    
    if preco_produto > 1000:
        mais_de_mil += 1
    if quantidade_produto == 1 or preco_produto < valor_barato:
        valor_barato = preco_produto
        nome_barato = nome_produto
    
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print("{:-^40}".format( "FIM DO PROGRAMA" ))
print(f'Dos {quantidade_produto} produtos cadastrados temos: O total gasto de: {total_gasto:.2f}.\nOs que custam mais que mil: {mais_de_mil} Produto(s).\nSendo o produto mais barato: {nome_barato} no valor de {valor_barato} ')

