#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.


soma = 0 #isso  é um acumulador!
cont = 0 #isso é um contador!

for c in range (1, 501, 2):
    if c % 3 == 0: # se o C for divisivel por 3
        soma = soma + c #ou podemos fazer soma += c
        cont = cont + 1 #ou podemos fazer cont += 1
print(f'A soma dos {cont} valores é: {soma}')