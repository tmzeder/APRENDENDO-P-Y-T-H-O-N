#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu Nome Completo: ')).strip() # Elimina antes e depois os espaços!

print('Analisando seu nome... ')

print(f'Seu nome em Maiúsculas é: {nome.upper()}\n E Seu nome em Minúsculas é: {nome.lower()}\n Seu Primeiro nome tem {nome.find(" ")} letras\n Seu nome tem ao todo {len(nome) - nome.count(" ")} letras!\n ')