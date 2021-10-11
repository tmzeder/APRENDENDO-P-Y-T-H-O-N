#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

#Com variaveis:

dist = float(input('Qual a distancia Percorrida? '))
print(f'Você está prestes a começar uma viagem de {dist}Km')
cost1 = dist * 0.50
cost2 = dist * 0.45

if dist <= 200:
    print(f'Até 200km de distância, a passagem custará: R${cost1:.2f}.')
else:
    print(f'A passagem custará: R${cost2:.2f} para viagens acima de 200km.')
    
    #maneira Simplificada com IF em linha ou Ternario!
    
dist = float((input('Informe a distância: '))) 
print(f'Você está prestes a começar uma viagem de {dist}Km')  
preco = dist *0.50 if dist <= 200 else dist *0.45

print(f'A sua viagem custará:R${preco:.2f}')
    
    
    #outra lógica de ser feito:
    
dist = float(input('Informe a Distância:'))
print(f'Você está prestes a começar uma viagem de {dist}Km')
print(f'Até 200Kkm o custo será de:R${dist*0.50}\n Para viagens mais longas, o custo será de: R${dist*0.45} ')