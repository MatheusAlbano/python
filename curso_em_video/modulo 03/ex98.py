from time import sleep

def contador(i, f, p):
    print('-='*30)
    if p == 0:
        p = 1
    elif p < 0:
        p = -(p)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        for num in range(i, f+1, p):
            print(num, end=' ')
            sleep(0.5)
    else:
        for num in range(i, f-1, -p):
            print(num,end=' ')
            sleep(0.5)
    print('FIM')
        

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)

