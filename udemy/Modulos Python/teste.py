

def calcular_Fat(n):
    contador = 1
    fatorial = 0
    while n >= contador:
        resultado = n*contador
        print(f'{n} X {contador} = {resultado}')
        contador+=1
        fatorial += resultado
    print(f'{n}! = {fatorial}')
    return fatorial

calcular_Fat(10)
    
