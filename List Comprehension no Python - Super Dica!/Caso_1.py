#Dobrar o valor de um produto!

#Exemplo normal:

lista_precos = [500, 1000, 2000, 3000, 25]

nova_lista = []
for preco in lista_precos:
    nova_lista.append(preco *2)
print(nova_lista)


#Exemplo Com LC:

nova_lista2 = [preco *2 for preco in lista_precos] #o preco vezes 2 será arescentado para cada item da lista de precos
print(nova_lista2)