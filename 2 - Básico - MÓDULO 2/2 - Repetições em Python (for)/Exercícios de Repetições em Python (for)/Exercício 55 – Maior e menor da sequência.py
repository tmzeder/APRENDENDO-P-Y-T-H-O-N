#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menorpeso = 0
maiorpeso = 0

for c in range (1, 6):
    peso = float(input(f'Informe o peso da {c}ª pessoa: '))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O menor peso lido foi: {menorpeso}KG e o Maior peso lido foi: {maiorpeso}KG')
    