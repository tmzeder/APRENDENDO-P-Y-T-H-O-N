#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

nome = str(input('Qual seu nome? '))
if nome == 'Thomaz':
    print('Que nome lindo você tem!') #este bloco só executa se a condição for verdadeira, ou seja, quando o nome for Thomaz ( Variavel)

print(f'Bom dia! {nome}')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1+n2)/2

if media >=6 :
    print('Sua média foi boa! Parabens!!! ')
else:
    print('Sua média foi Regular!!! Estude mais! ')   