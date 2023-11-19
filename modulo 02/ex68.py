from random import randint

n = cont = soma = 0
resultado = ['PAR','ÍMPAR']
while True:
    print('-='*20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*20)
    n = int(input('Diga um valor: '))
    pi = input('Par ou Ímpar? [P/I] ').strip().upper()
    computador = randint(0,11)
    soma = n + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    
    print('-'*45)
    print(f'Você jogou {n} e computador {computador}. Total de {soma} DEU {resultado}')

    if soma % 2 == 0 and pi == 'P':
        cont += 1
    elif soma % 2 != 0 and pi == 'I':
        cont += 1
    else:
        print('-'*45)
        print('Você PERDEU!')
        print('=-'*20) 
        break
    print('-'*45)
    print('Você VENCEU!')
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {cont} vezes.')

