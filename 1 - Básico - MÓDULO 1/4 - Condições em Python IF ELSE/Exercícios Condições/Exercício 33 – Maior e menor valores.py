# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
n3 = int(input("Terceiro Valor: "))

# Testando o Menor!

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3


print(f"O Menor valor é: {menor}")

# Testando o Maior!

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O Maior valor é:{maior}")
    
