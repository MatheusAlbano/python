from uteis import números

num = int(input('Digite um valor: '))
fat = números.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {(números.dobro(num))}')