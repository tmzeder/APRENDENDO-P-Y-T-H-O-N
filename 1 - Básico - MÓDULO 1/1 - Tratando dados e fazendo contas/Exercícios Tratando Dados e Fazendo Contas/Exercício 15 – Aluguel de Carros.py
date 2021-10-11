#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Kilometros percorridos: KM '))
dia = int(input('Quantidade de dias alugados '))
total_a_pagar = (60*dia)+(km*0.15)

print(f'O Total a ser pago é de: R${total_a_pagar:.2f}')
                