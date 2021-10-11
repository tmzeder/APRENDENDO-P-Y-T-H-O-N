frase = 'Curso em Vídeo Python'
print(frase[3]) # o sistema Python começa a contar a partir do 0 ZERO que no caso é a letra C!

frase = 'Curso em Vídeo Python'
print(frase[3:13]) # o sistema Python começa a contar a partir do 3 que no caso é a letra S e vai até o 13 que seria a letra E de VIDEO!

frase = 'Curso em Vídeo Python'
print(frase[:13]) # o sistema Python começa a contar a partir do inicio e vai até onde se localiza a Letra E da palavra VIDEO!

frase = 'Curso em Vídeo Python'
print(frase[3:13:2]) # o sistema Python começa a contar a partir do inicio e vai até onde se localiza a Letra E da palavra VIDEO, porém agora pulando de duas em duas casas!

frase = 'Curso em Vídeo Python'
print(frase[::2]) # o sistema Python começa a contar a partir do inicio e vai até o fim pulando de 2 em duas casas!


print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().""")

frase = 'Curso em Vídeo Python'
print(frase.upper().count('o')) #contagem da letra "o" em maiuscula!

frase = 'Curso em Vídeo Python'
print(len(frase)) #tamanho da frase

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android')) ##troca 

frase = 'Curso em Vídeo Python'
print(frase.lower().find('python'))#encontrar em minusculo!

frase = 'Curso em Vídeo Python'
print(frase.upper().find('android'))#encontrar em maiusculo! Ele não encontra e me retorna -1

frase = 'Curso em Vídeo Python '
dividir = frase.split()
print(dividir[0]) #aqui a frase foi dividida e como no print temos a variavel com colchetes e o zero dentro, o interpretador pegará apenas o inicio.

frase = 'Curso em Vídeo Python '
dividir = frase.split()
print(dividir[0] [3]) #Já neste exemplo se eu mandar ele pegar do inicio e acrescentar outro colchete com, por exemplo o numero 3, ele me mostra a posição 3 da letra dentro da lista [0] Zero.