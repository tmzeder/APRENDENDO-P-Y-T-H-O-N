#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Velocidade Do Veículo: '))
multa = (vel - 80) * 7 #lógica!

if vel > 80:
    print(f'Você foi multado em: R${multa:.2f} O limte é de 80Km')
else:
    print('Você não foi Muultado! ')