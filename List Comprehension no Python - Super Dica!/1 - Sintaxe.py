#Basicamente a List Comprehension é ultlizada para EU baseado no iteravel, gerar um iteravel e no caminho fazer um processamento de dados!

numeros = [1, 2, 3, 4, 5]
novos_numeros = [numero for numero in numeros]
print(novos_numeros)

#Acima seria o mesmo que fazer:

novos_numeros = []
for numero in numeros:
    novos_numeros.append(numero)
print(novos_numeros)