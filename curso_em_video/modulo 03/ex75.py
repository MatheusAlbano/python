num = (int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: ')),)

print(f'Você digitou os valores {num}')
print(f'A) O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'B) O valor 3 foi digitado na {num.index(3)+1}ª posição.')
else:
    print('B) O valor 3 não foi digitado nenhuma vez.')
print('C) Os valores pares digitados foram ',end='')

for n in num:
    if n%2==0:
        print(n,end=' ')
print('0.')

            