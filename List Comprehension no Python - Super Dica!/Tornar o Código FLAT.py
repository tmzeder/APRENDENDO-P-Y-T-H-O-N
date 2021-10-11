  
numeros = [[numero, numero ** 2] for numero in range(10)] #Lista dentro de Lista - Para o numero de zero a dez, numero elevado ao quadrado
flat = [y for x in numeros for y in x] #para lista X dos numeros, para lista Y no X
print(numeros)
print(flat)