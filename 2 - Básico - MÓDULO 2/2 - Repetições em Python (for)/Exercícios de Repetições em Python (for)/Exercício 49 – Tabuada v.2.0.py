# Refaça o EXERCÍCIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


tab = int(input("Digite um valor para ver sua Tabuada!: "))

for c in range(1, 11):
    print(f"{tab} x {c:2} = {tab * c}")
print("Fim")
