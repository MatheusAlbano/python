valores = list()

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    opcao = input('Quer continuar? [S/N] ').strip().upper()
    if opcao != 'S':
        break
print('-='*20)
print(f'Você digitou os valores {valores}')




    