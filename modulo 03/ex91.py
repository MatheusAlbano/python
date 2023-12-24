from random import randint
from time import sleep
from operator import itemgetter

numeros_sorteados = dict()
print('Valores sorteados:')
for c in range(1,5):
    numeros_sorteados[f'jogador{c}'] = randint(1,6)
    print(f'    O jogador{c} tirou {numeros_sorteados[f"jogador{c}"]}')
    sleep(1)

ranking = list(sorted(numeros_sorteados.items(), key=itemgetter(1), reverse=True))
print('-='*20)
print('== Ranking dos jogadores ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)



