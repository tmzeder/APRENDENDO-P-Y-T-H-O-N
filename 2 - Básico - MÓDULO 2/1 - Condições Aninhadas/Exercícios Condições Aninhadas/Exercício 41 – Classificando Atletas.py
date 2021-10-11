#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

from datetime import date


ano_nasc = int(input('Informe o Ano de Nascimento: '))
atual = date.today().year #ano atual
idade = atual - ano_nasc

if idade <= 9:
    print(f'Sua idade é {idade} anos, Classificação MIRIM!')
elif idade > 9 and idade <= 14:
    print(f'Sua idade é {idade} anos. Classificação INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'Sua idade é {idade} anos. Classificação JUNIOR!')
elif idade > 19 and idade <= 25:
    print(f'Sua idade é {idade} anos. Classificação SÊNIOR!')
else: 
    print(f'Sua idade é {idade} anos. Classificação MASTER!')
