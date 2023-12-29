jogador = dict()
partidas = list()
totgols = 0
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1,tot+1):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    totgols += partidas[c-1]
jogador['gols'] = partidas
jogador['total'] = totgols
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
   print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i, a in enumerate(partidas):
    print(f'     => Na partida {i+1}, fez {partidas[i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')




    