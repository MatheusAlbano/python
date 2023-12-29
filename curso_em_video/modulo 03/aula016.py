lanche = ('Hambúrguer','Suco','Pizza','Pudim')
# Tuplas são IMUTÁVEIS

for cont in range(0, len(lanche)):

    if lanche[cont] != 'Suco':
        print(f'Eu vou comer {lanche[cont]}')
    else:
        print(f'Eu vou tomar {lanche[cont]}')

print('Comi pra caramba!')

for comida in lanche:
    if comida != 'Suco':
        print(f'Eu vou comer {comida}')
    else:
        print(f'Eu vou tomar {comida}')

print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    if comida != 'Suco':
        print(f'Eu vou comer {comida} na posição {pos}')
    else:
        print(f'Eu vou tomar {comida} na posição {pos}')

print('Comi pra caramba!')