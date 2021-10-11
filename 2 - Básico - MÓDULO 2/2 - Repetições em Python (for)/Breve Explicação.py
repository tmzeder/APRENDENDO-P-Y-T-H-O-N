for c in range(1, 6): # de 1 a 6 ele conta até 5 sem considerar o ultimo
    print('Olá')
print('Fim do Programa.')

    # quando colocamos -1 indicamos que a contagem será feita de 6 para 0
for c in range(6, 0, -1):
    print(c)
print('Fim do Programa.')

for c in range(0, 7, 2): # Aqui ele conta de 0 até 7 pulando de 2 em 2
    print(c)
print('Fim do Programa.')

i = int(input('Inicio '))
f = int(input('Fim '))
p = int(input('Pula '))
for c in range(i, f+1, p):
    print(c)
print('Fim do Programa.')

soma = 0
for c in range(0, 3): 
    n = int(input('Digite um valor: '))
    soma = soma + n #ou pode colocar soma += n, que também funciona
print(f'A soma dos Valores foi: {soma}') # ou podemos criar a variavel com a conta dentro do couchete! ou seja, a soma dos valores foi: {soma += n}, que será aceito