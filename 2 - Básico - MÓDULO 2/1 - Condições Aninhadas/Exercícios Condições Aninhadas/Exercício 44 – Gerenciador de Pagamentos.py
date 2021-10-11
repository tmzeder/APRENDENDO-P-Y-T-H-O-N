#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format (' Lojas THOMAZ '))

p = float(input('Informe o Preço: '))

print('''Formas de Pagamento: 
[1] À Vista / Dinheiro/Cheques
[2] À Vista no Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão ''')

op = int(input('Irforme a Opção: '))

if op == 1:
    total = p - ( p * 10 / 100)
    print(f'O valor total é de {total:.2f} com 10% de Desconto!')
elif op == 2:
    total = p - (p * 5 / 100)
    print(f'O valor total é de {total:.2f} com 5% de Desconto!')
elif op == 3:
    total = p
    parcela = p / 2
    print(f'O valor total é de R${p:.2f} e a parcela ficará no valor de R${parcela:.2f}')
elif op == 4:
    total = p + (p *20 / 100)
    totparc = (int(input('Informe a quantidade de parcelas: ')))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc} vezes COM JUROS\n  No valor de R${total:.2f} e as parcelas serão de R${parcela:.2f}')
    print(f'Sua compra de R${p:.2f}, vai custar R${total:.2f} no final.')
else:
    total = 0
    print('Opção inválida! Tente novamente!')


