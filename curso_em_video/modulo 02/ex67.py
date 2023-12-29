n = cont = 0

while True:
    cont = 1
    print('-'*45)
    n = int(input('Você quer ver a tabuada de qual número: '))
    print('-'*45)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n*cont}')
        cont += 1
print('FIM')