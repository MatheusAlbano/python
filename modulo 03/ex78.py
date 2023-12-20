valores = list()
men = 0
mai = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]


print('-='*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posições ',end='')

for i,v in enumerate(valores):
    if v == mai:
        print(f'{i}... ',end='')
print()

print(f'O menor valor digitado foi {men} nas posições ',end='')
for i,v in enumerate(valores):
    if v == men:
        print(f'{i}... ',end='')
print()
print('-='*20)