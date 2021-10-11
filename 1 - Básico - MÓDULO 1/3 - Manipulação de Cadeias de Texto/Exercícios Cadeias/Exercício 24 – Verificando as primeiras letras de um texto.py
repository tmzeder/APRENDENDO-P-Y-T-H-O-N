#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Iforme a Cidade: ')).strip()

print(cid[:5].capitalize() == 'Santo') # printa a variavel da cidade especifica com : onde se inicia sabendo que SANTO que a contagem começa no ZERO ou seja: 0=S 1=a 2=n 3=t 4=o. Sendo assim a contagem deve ser 5! E colocar  == que significa IGUAL em Python.