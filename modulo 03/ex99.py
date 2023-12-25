from time import sleep

def maior(* valores):
    print('-='*30)
    print('Analisando todos os valores passados...')
    for v in valores:
        print(f'{v} ',end='')
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo.')   
    if valores == ():
        print('O maior valor informado foi 0.')
    
    else: 
        print(f'O maior valor informado foi {max(valores)}.')


    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()