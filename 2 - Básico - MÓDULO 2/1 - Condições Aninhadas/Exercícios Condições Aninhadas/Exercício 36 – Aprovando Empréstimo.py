#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor do Imóvel: R$ '))
salario = float(input('Salário do Comprador: R$ '))
anos = int(input('Anos de Financiamento: '))

minimo = salario * 30/100
prest = casa / (anos*12) # Preço da casa divido por quantos meses a pessoa vai pagar! e para saber quantos meses, fazemos os anos vezes 12

print(f'Para pagar um imóvel de {casa} em {anos} anos\n A prestação será de: {prest:.2f} ')

if prest <= minimo:
    print('CONCEDIDO')
else:
    print('NEGADO')