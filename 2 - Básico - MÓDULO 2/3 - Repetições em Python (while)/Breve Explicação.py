''' for c in range (1, 10):
    print(c)
print('Fim do programa.')'''  #O mesmo pode ser representado em While

c = 1
while c < 10:
    print(c)
    c = c + 1 # ou c += 1
print('Fim do programa.')

'''for c in range (1, 5):
    num = int(input('Informe um valor: '))
print('Fim do programa.')'''

num = 1
while num != 0:
    num = int(input('Informe um valor: ')) #FEITO EM WHILE O EXEMPLO ACIMA
print('Fim do programa.')

resposta = 'S'

while resposta == 'S':
    num = int(input('Informe um valor: '))
    resposta = str(input('Deseja continuar? [S/N]? ')).upper()
print('Fim do programa.')


num = 1
par = impar = 0

while num != 0:
    num = int(input('Informe um valor: '))
    if num != 0:
        if num % 2 == 0: # neste campo "se o numero digitado for par/ divisivel por 2 e restar 0"
            par += 1
        else: impar += 1
print(f'Você digitou {par} números pares e {impar} números impares.')
