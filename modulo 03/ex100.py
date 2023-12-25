from random import randint
from time import sleep

def sortear():
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(0,5):
        lista.append(randint(1,10))
        print(f'{lista[c]}',end=' ')
        sleep(0.5)
    print('PRONTO!')
    
def somapares(lista):
    sompar = 0
    for l in lista:
        if l % 2 == 0:
            sompar += l
    print(f'Somando os valores pares de {lista}, temos {sompar}.')

lista = []
sortear()
somapares(lista)





