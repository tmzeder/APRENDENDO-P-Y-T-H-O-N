#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# Para representar cores no python usamos: \033[m Lembre-se de fechar com a letra m! dentro desse comando ultilizamos 3 valores, um para estilo, um para texto e outro pra background, separando os mesmos por ; ponto é virgula!


print('\033[0;30;41mThomaz Eder\33[m') #dentro da string

n = 2
n1 = 4

print(f'os valores são: \033[32m{n}\033[m e \033[33m{n1}')


# Dicionário de cores!!!

nome = 'Thomaz'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto_branco':'\033[7;30m'} # Dicionário de cores é feito em chaves! PARA SEPARAR AS VARIAVEIS DENTRO DO DICIONÁRIO USAMOS VIRGULA!

print(cores['azul'], nome, cores['limpa'])