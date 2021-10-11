#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date

nasc = int(input('Informe o Ano de nascimento: '))
atual = date.today().year #ano atual
idade = atual - nasc
print(f'Quem nasceu em {nasc}, tem {idade} anos em {atual}!')

if idade < 18:
    print(f'Ainda não esta na hora de se alistar, ainda faltam {18 - idade} anos para o alistamento!')
elif idade > 18:
    print(f'Você possui {idade} anos , Você devria ter se alistado há {idade - 18} anos atrás!')
else:
    print(f'Você possui {idade} anos, Aliste-se Imediatamente!')