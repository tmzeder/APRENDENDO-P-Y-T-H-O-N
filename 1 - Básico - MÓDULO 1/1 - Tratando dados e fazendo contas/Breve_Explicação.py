nome = input('Qual seu nome? ')
print(f'Olá {nome:_^10} muito prazer em conhecê-la(o) ')
#Dentro das Chaves os dois pontos simbolizam oque pode ser acrescentado, no caso o _ dez vezes, porem antes temos o acento ^ que permite que a palavra fique centralizada nos 10 caracterers

n1 = int(input('digite um nº'))
n2 = int(input('digite outro nº'))
s = n1+n2 #SOMA
m = n1*n2 #MULTIPLICAÇÃO
d = n1/n2 #DIVISÃO
di = n1//n2 #DIVISÃO INTEIRA
e = n1**n2 # EXPONECIAÇÃO
print(f'A soma é de: {s} \n A multiplicação é de : {m} \n A divisão é de: {d:.3f} \n A Div Inteira é: {di} \n A Exponenciação é de: {e:.2f}')