#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
#O comando \n pula linhas!!! o f antes dos apostrofos simboliza que vamos formatar o print colocando as variaveis dentro das chaves{}

var = input('Digite algo ' )
print(f'O tipo primitivo desse valor é: {type(var)}\n esse valor tem espaços? {var.isspace()}\n esse valor é um numnero? {var.isnumeric()}\n Está em Maiusculas? {var.isupper()}\n é alfanumerico? {var.isalnum()}' )
