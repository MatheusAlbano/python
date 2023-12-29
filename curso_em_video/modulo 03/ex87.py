matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
sompar = somter = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if l == 1 and c == 0:
            mai = matriz[1][0]
        if matriz[l][c] % 2 == 0:
            sompar += matriz[l][c]
        if c == 2:
            somter += matriz[l][c]
        if l == 1:
            if matriz[1][c] > mai:
                mai = matriz[1][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {sompar}')
print(f'A soma dos valores da terceira coluna é {somter}')
print(f'O maior valor da segunda linha é {mai}')