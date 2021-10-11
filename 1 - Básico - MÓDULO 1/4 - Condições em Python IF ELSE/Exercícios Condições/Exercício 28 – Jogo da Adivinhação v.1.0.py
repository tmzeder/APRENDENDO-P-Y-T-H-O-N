#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

    from random import randint #randomiza um numero INTEIRO aleatório!
    from time import sleep

pc = randint(0, 5)#faz o PC sortear um número aleatório.
print('=-='*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar! ...')
print('=-='*20)
jogador = int(input('Em que número eu pensei? ')) #o Usuário tenta adivinhar o número!

print('PROCESSANDO. . . ')
sleep(2)

if jogador == pc:
    print('Você venceu!!!')
else:
    print(f'Você perdeu! Eu pensei no {pc} e não no {jogador}')





       
    