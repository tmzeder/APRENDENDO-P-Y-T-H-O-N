#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão # a matemática diz que o henezimo termo de uma PA ( progressão aritmética)
for c in range (primeiro, décimo + razão, razão):
    print(f'{c}' , end=' → ')
print('Fim do Programa.') 