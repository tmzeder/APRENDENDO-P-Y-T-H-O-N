#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mediaidade = 0
somaidade = 0
maioridadehomem = 0
maisvelho = ''
mulher20 = 0

for c in range (1, 5):
    print(f'----- {c}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]? ')).strip()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 = mulher20 + 1 
           
mediaidade = somaidade / 4
print(f'A média da idade do grupo é de {mediaidade:.1f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {maisvelho}')
print(f'Ao todo são {mulher20} Mulheres com menos de 20 anos')
