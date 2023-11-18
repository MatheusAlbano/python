n = int(input("Digite um número para calcular seu Fatorial: "))
contador = n
f = 1
print('Calculando {}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ',end='')
    f *= contador
    contador -= 1

print(f)
