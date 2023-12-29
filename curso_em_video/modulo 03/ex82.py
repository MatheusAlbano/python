valores = list()
pares = list()
impar = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Quer continuar? [S/N] ').strip().upper()
    if opcao != 'S':
        break

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)

print('-='*30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impar}')


