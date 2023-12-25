def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-'*20)

def contador(*núm):
    for valor in núm:
        print(f'{valor} ',end='')
    print('FIM!')
    print('-'*20)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
    pos += 1


#Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=4, a=3)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 9, 8, 5, 7]
dobra(valores)
print(valores)


