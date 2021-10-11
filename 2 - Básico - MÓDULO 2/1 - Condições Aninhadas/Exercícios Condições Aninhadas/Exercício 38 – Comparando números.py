# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

num = int(input("Informe o 1º Número Inteiro: "))
num2 = int(input("Informe o 2º Número Inteiro: "))

if num > num2:
    print(f"O Valor {num} é o Maior Valor!")
elif num < num2:
    print(f"O Valor {num2} é o Maior Valor!")
elif num == num2:
    print("Não existe valor maior, os dois são iguais!")
