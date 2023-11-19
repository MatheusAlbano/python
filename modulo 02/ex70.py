preco = total = cont = totmil = menor = 0
nome = continuar = barato = ''


while True:
    print('-'*30)
    print('{:^30}'.format('LOJA SUPER BARATÃO'))
    print('-'*30)
    continuar = 'S'
    while continuar == 'S':
        nome = input('Nome do Produto: ')
        preco = float(input('Preço: R$'))
        total += preco
        cont += 1
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if preco > 1000:
            totmil += 1
        if cont == 1 or preco < menor:
            menor = preco
            barato = nome
        while continuar not in 'SN':
            continuar = input('Quer continuar? [S/N] ').strip().upper()

    break
print('-'*10,'FIM DO PROGRAMA','-'*10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos cadastrados custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
