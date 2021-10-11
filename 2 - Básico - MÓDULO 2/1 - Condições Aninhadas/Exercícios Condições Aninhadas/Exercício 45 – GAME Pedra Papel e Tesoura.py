#Crie um programa que faça o computador jogar Jokenpô com você.


from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)

print('''Suas Opções:
[0] Pedra!
[1] Papel!
[2] Tesoura!''')

jogador = int(input('Qual sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

print(f'O computador escolheu {itens[comp]}') #o computador escolheu um item na posição comp
print(f'O Jogador Jogou: {itens[jogador]}')

if comp == 0: # O Computador jogou: Pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você Ganhou! :]')   
    elif jogador == 2:
        print('Coputador Ganhou :[')
    else:
        print('Jogada Inválida!')
elif comp == 1: # O Computador jogou: Papel
    if jogador == 0:
       print('Coputador Ganhou :[')          
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você Ganhou! :]')
    else:
        print('Jogada Inválida!')
elif comp == 2: # O Computador jogou: Tesoura
    if jogador == 0:
        print('Você Ganhou! :]')
    elif jogador == 1:
        print('Coputador Ganhou :[')
    elif jogador == 2:
       print('Empate!') 
    else:
        print('Jogada Inválida!')
        
