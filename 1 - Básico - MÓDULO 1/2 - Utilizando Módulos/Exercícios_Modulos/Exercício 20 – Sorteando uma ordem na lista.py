#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

al1 = input('Nome do Aluno: ')
al2 = input('Outro Aluno: ')
al3 = input('Outro Aluno: ')
al4 = input('Outro Aluno: ')
lista = [al1, al2, al3, al4]
random.shuffle(lista) # o comando shuffle mistura as variaveis dentro da lista!
print(f'A Ordem de apresentação será: {lista}!')
