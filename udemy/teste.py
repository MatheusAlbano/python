def calcular_fatorial(numero:int):
    if numero == 1:
        return 1
    else:
        return numero*calcular_fatorial(numero-1)
    
print(calcular_fatorial(5))
