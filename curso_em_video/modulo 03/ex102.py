def fatorial(num, show=False):
    """
    fatorial(num, show=False)
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n. 
    """
    f = 1
    print('-'*30)
    for c in range(num,0,-1):
        f *= c
        if show == True:
            if c > 1:
                print(f'{c} x ',end='')
            elif c == 1:
                print(f'{c} = ',end='')
    return f


#Programa Principal
print(fatorial(6,True))



