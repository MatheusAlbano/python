def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início do contagem
    :param f: fim do contagem
    :param p: passo da contagem
    :return: sem retorno
    """  #Docstring
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM')

def somar(a=0, b=0, c=0):
    """
    -> Soma Três números e exibe o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

def teste(b):
    global a 
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

def somar_return(a=0,b=0,c=0):
    s = a + b +c
    return s


#Programa Principal
a = 8
teste(a)
print(f'A fora vale {a}')
somar(3, 2, 7)
somar(4, 5)
somar(3)
r1 = somar_return(4, 5, 7)
r2 = somar_return(6, 7)
r3 = somar_return(9)
print(f'Os resultados foram {r1}, {r2} e {r3}')
#help(contador)

