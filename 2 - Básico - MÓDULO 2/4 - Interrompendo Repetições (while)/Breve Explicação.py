'''O Comando BREAK quebra um loop que está acontecendo em uma sequencia de vezes'''
'''Exemplo:'''

'''contador = 1
while True:
    print(contador, '→ ', end='')
print("Acabou")
Exemplo de loop infinito ↑'''



'''n = 0 # inicia a variavel numero com 0
while n != 999: # enquanto  a variavel n for diferente de 999:
    n = int(input('Informe um número: '))#informar o número para ser armazenado na variavel n.'''
'''Quando o valor 999 for digitado o programa se encerra, chamamos isso de flag ou seja, o 999 é o flag! Caso o número 999 não seja digitado,  o programa continuará a pedir um número.'''

num = soma = 0
while num != 999:
    num = int(input('Informe um Número: '))
    soma += num #Soma recebe Soma + Numero
print(f'A soma vale: {soma}!') #O resultado mostrará a soma juntamente com o 999, o que é cosiderado errado pois querem os saber a soma apenas dos números digitados sem incluir o 999.

'''Abaixo a maneira com Loop Infinito e correta a ser feita: '''

num = soma = 0 #A variavel num  e soma recebem 0
while True: #enquanto for verdade:
    num = int(input('Informe um número: '))
    if num == 999:# se o número informado for igual a 999 o  programa para e executa a soma abaixo
        break
    soma += num
print(f'A soma vale: {soma}.')


'''f string
Relembrando:
nome = 'José'
idade = (33)
salario = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
print(f'Esse nome {nome:20} é lindo') #20 espaços
print(f'Esse nome {nome:^20} é lindo') #20 espaços centralizado
print(f'Esse nome {nome:-^20} é lindo') #20 espaços centralizado com traço
print(f'Esse nome {nome:-<20} é lindo') #alinhado a esquerda
print(f'Esse nome {nome:->20} é lindo') #alinhado a direita'''