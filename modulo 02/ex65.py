n = cont = soma = maior = menor = media = 0
opcao = 'S'

while opcao == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    opcao = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior}  e o menor foi {menor}')
