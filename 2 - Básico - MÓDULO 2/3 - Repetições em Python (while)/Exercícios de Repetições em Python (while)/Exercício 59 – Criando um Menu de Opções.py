'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''


from time import sleep

num1 = int(input('Informe o 1º valor: '))
num2 = int(input('Informe o 2º valor: '))
opção = 0
while opção != 5:
    print(''' [1] Somar.
 [2] Multiplicar.
 [3] Maior Valor.
 [4] Novos Numeros.
 [5] Sair do Programa.''')
    opção = int(input('→ → → Selecione a Opção Desejada: '))
    if opção == 1:
        soma = num1 + num2
        print(f'A Soma entre {num1} e {num2} é: {soma}')
    elif opção == 2:
        produto = num1 * num2
        print(f'O resultado de {num1} x {num2} é: {produto}')
    elif opção == 3:
        if num1 > num2:
            maior = num1
        elif num1 < num2:
            maior = num2
        print(f'Entre {num1} e {num2} o maior valor é: {maior}')
    
        
        
    elif opção == 4:
        print('Informe os novos valores: ')
        num1 = int('Informe o 1º valor:')
        num2 = int('Informe o 2º valor: ')

    elif opção == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida, tente novamente. ')
    print('=-=' * 10)
    sleep(2)
print('FIM DO PROGRAMA.')
