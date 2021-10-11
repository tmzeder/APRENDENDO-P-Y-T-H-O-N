#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('Analisador de Triângulos!')
print('-='*20)

r1 = float(input('Informe a Primeira Reta: '))
r2 = float(input('Informe a Segunda Reta: '))
r3 = float(input('Informe a Terceira Reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

    print(f'Os Segmentos {r1, r2, r3}, Podem formar um Triângulo!')
else:
    print(f'Os Segmentos {r1, r2, r3}, NÃO podem formar um Triângulo!') #Dentro de Couchetes separamos variaveis com VIRGULAS!!