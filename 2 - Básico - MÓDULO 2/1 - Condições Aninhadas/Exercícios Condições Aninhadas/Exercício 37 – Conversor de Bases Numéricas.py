#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


num = int(input('Informe um número Inteiro!: '))
print('Digite [1] para Binário!, [2] para Octal! ou [3] para Hexadecimal!')
op = int(input('Sua Opção: '))

if op == 1:
    print(f'O número escolhido em Binário é: {bin(num)[2:]}')
elif op == 2:
    print(f'O número escolhido em Octal é: {oct(num)[2:]}')
elif op == 3:
    print(f'O número escolhido em Hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção Inválida! Tente novamente!')
    #[2] local de inicio! bin, oct e hex ja estão disponiveis na linguagem python!