#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input(' Digite seu salário: R$'))
novo = (s *15/100) + s

print(f'Seu salário com 15% de aumento é de: R${novo:.2f}')