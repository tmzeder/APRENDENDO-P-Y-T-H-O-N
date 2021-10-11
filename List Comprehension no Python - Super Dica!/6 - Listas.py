nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}' #A ultima letra de cada nome fica maiuscula e as demais minusculas
    for nome in nomes
]
print(novos_nomes)