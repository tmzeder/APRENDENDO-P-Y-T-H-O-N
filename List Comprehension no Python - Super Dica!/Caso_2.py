#Todos os produtos que custarem acima de #1.000 Dolares Imposto de 50% sobre o valor total!

'''lista_precos = [500, 1000, 2000, 3000, 25]

imposto = []
for cpreco in lista_precos:
    if cpreco > 1000:
        imposto.append(cpreco * 0.5)
print(f'O valor adicionado foi de {imposto}')

#Exemplo Com LC: 

imposto2 = [cpreco * 0.5 for cpreco in lista_precos if cpreco > 1000]
print(f'O valor adicionado foi de {imposto2}')'''

numero = int(input("Fatorial de: ") )

resultado=1
for c in range(1,numero+1):
    resultado *= c

print(resultado)