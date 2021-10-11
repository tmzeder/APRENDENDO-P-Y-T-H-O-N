'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('='*30)
print("{:-^30}".format( "BANK" ))# comando para centralizar uma string em tantos espaços, ou no caso, hifens
print('='*30)

valor_saque = int(input('Qual o valor desejado?: '))
total = valor_saque
cedulas = 50
contagem_cedulas = 0

while True:
    if total >= cedulas:
        total -= cedulas
        contagem_cedulas += 1
    else:
        if contagem_cedulas > 0:
            print(f'O total de {contagem_cedulas} cedulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        if cedulas == 20:
            cedulas = 10
        if cedulas == 10:
            cedulas = 1
        contagem_cedulas = 0
        if total == 0:
            break
print('Fim da Transação.')