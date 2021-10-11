#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

fr = str(input('Digite Algo: ')).upper().strip()

print(f'Letra A aparece: {fr.count("A")} Vezes!\nA primeira letra A aparece na posição: {fr.find("A")+1}\nA ultima letra A aparecena posição: {fr.rfind("A")+1}')