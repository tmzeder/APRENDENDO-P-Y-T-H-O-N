#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido
import random

al1 = input('Aluno 1: ')
al2 = input('Aluno 2: ')
al3 = input('Aluno 3: ')
al4 = input('Aluno 4: ')
lista = [al1, al2, al3, al4] # essa é uma lista que o Python reconehce quando usamos []
escolhido = random.choice(lista) # o camando choice, escolhe aleatoriamente!

print(f'O Aluno escolhido foi: {escolhido}!')
