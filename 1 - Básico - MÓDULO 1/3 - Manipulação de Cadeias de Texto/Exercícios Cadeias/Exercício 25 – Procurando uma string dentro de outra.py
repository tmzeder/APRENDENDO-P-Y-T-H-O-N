#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Informe o Nome: ')).strip()

print('Seu Nome tem Silva?', 'silva' in nome.lower ()) #LEMBRANDO QUE O IN É UM OPERADOR, OU SEJA, Contem silva em nome.lower?