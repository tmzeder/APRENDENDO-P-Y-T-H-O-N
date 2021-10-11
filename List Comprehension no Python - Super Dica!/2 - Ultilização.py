

numeros = [1, 2, 3, 4, 5]
divisão = [numero /2 for numero in numeros]
multiplicação = [numero *2 for numero in numeros]
square = [numero **2 for numero in numeros]

print(f'Lista Original{numeros}')
print(f'Lista com DIVISÃO: {divisão}')
print(f'Lista com MULTIPLICAÇÃO: {multiplicação}')
print(f'Lista AO QUADRADO: {square}')


#ultilizando funções COM RETORNO E COM PARAMETRO:


def divisãoFn(x, y):
    return x / y

def multiplicaçãoFn(x, y):
    return x * y

def potenciaçãoFn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]

divisão = [divisãoFn(numero, 2) for numero in numeros]
multiplicação = [multiplicaçãoFn(numero, 2) for numero in numeros]
quadrado = [potenciaçãoFn(numero, 2) for numero in numeros]

print(f'Lista Original{numeros}')
print(f'Lista com DIVISÃO: {divisão}')
print(f'Lista com MULTIPLICAÇÃO: {multiplicação}')
print(f'Lista AO QUADRADO: {square}')