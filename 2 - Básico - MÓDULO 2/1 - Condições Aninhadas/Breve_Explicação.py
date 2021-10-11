
#podem ser colocados quantos elifs forem necessários!, nunca esquecer do :

nome = str(input("Seu nome: ")).capitalize()

if nome == "Thomaz":
    print(f"Olá {nome} Que nome bonito!")
elif nome == "Ana" or nome == "Pedro" or nome == "Jacqueline":
    print("Seu nome é bem popular")
elif nome in "Jessica Helena Maria Juliana":  # 'se não se' em nome...
    print("Que belo nome feminino!")
else:
    print("Que nome normal")
print("Tenha um bom dia!")
