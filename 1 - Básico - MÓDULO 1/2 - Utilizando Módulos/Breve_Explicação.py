#inportações de bibliotecas, sempre devem ser feitas na primeira linha do código!
#PODEMOS IMPORTAR ALGO UNICO DE DENTRO DA BIBLIOTECA COM O COMANDO from math import sqrt ( por exemplo), ou seja,  estamos dizendo: "da Biblioteca math, importe somente sqrt"

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} vai ser {raiz:.2f} !')