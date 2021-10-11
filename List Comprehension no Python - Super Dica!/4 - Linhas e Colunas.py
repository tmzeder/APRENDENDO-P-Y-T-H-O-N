

linhas_e_colunas = [
    (x, y)
    if y != 2 else (x, y * 1000) #se aparecer o 2 multiplica-se Y por Mil
    for x in range(1, 11) #Quando temos dois FOR em sequencia, significa que são FOR Aninihados e não 2 diferentes
    for y in range(1, 6)
    if x != 2 #exemplo para não apaecer o numero 2
]

print(linhas_e_colunas)

for x in range(1, 11):  # FOR para linhas e aninhado nesse FOR
    for y in range(1, 6):  # TEMOS um for para colunas.
        print(x, y)
