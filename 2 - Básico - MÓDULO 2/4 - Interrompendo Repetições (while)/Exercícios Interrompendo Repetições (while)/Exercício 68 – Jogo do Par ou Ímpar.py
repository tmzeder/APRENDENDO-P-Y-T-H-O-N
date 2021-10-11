'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Digite [P/I} para Par ou Impar! ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O resultado foi: {total}')
    print(f'Deu PAR ' if total %2 == 0 else 'Deu IMPAR ')
    if tipo == 'P':
        if total %2 == 0:
            print('Você Ganhou! ')
            vitoria += 1
        else:
            print('Você Perdeu! ')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você Ganhou! ')
            vitoria += 1
        else:
            print('Você Perdeu! ')
            break
    print('Vamos Jogar novamente... ')
print(f'GAME OVER! Você venceu {vitorias} vezes! ')
