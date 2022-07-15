from random import randint
from time import time


lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('---')
word = str(input('Word: ')).split()


cont = 1
wordS = ''
start = time()

while True:
    for letter in range(len(word[0])):
        msg = lista[randint(0, len(lista) - 1)]
        wordS += msg

    end = time()

    if len(word) > 1:
        limit = int(word[1])
    
        if cont == limit:
            print(wordS, f'{(end - start):.5f}')
            print(cont)
            break

    if wordS == word[0]:
        print(wordS, f'{(end - start):.5f}')
        print(cont)
        break

    print(wordS, f'{(end - start):.5f}')
    cont += 1
    wordS = ''
    