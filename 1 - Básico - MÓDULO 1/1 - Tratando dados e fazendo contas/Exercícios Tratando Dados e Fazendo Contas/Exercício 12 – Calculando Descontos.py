#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Preço do Produto: R$'))
desc = preco * 5/100 
print(f'O DESCONTO de 5% É de: R${desc:.2f}, e o você paga no produto: R${preco - desc}')

