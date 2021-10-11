#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sa = float(input('Salário Atual: R$'))

if sa <= 1250: 
    print(f'Se você ganha R${sa}, seu novo salário será de: {sa + (sa*15/100) :.2f}')
else:
    print(f'Se você ganha R${sa}, seu novo salário será de:{sa + (sa *10/100):.2f}')
    