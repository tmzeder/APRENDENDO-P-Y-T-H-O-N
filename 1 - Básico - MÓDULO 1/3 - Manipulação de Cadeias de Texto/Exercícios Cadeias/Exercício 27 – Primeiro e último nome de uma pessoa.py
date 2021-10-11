# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Iforme o Nome completo: ")).strip()
nome = n.split()#Dividimos a variavel

print(f"Seu primeiro nome é: {nome[0]} E seu Ultimo nome é: {nome[len(nome)-1]}")#chamamos a primeira posição com 0 e a ultima posição, chamamos a variavel em colchetes len para saber o tamanho dela -1!
