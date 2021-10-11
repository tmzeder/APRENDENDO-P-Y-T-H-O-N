#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

money = float(input('Dinheiro: R$ '))
print(f'Você pode comprar US${money/5.70:.2f} Dólares')