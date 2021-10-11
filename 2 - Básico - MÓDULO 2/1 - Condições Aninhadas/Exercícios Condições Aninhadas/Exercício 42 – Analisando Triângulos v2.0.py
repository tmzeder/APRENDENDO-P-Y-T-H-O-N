#Refaça o DESAFIO 35 dos triângulos "#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."  , acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

print('-='*20)
print('Analisador de Triângulos!')
print('-='*20)

r1 = float(input('Informe a Primeira Reta: '))
r2 = float(input('Informe a Segunda Reta: '))
r3 = float(input('Informe a Terceira Reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os Segmentos {r1, r2, r3}, Podem formar um Triângulo!', end = '')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: #!=  Símbolo de Diferente!
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print(f'Os Segmentos {r1, r2, r3}, NÃO podem formar um Triângulo!')