'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''


from random import randint #randomiza um numero INTEIRO aleatório!
computador = randint(0, 10)
print('Sou seu computador, acabei de pensar em um número entre zero e dez! ')
print('Será que você adivinha qual é? ')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos... tente novamente!')
print(f'Acertou com {palpites} tentativas!')