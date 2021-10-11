#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero  = int(input('Informe um numero: '))
u = numero // 1 % 10 # Matemáticamente falando podemos dividir a variavel U pelo NUMERO atraves da divisão inteira // e dividir novamente dessa vez com % para saber o resto da divisão
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analisando o Numero Digitado...')
print(f' Unidade: {u}\n Dezena: {d}\n Centena: {c}\n Milhar: {m}\n')

