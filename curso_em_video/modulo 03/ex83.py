expr = input('Digite a expressão: ')
lista_abert = []
lista_fech = []
for símb in expr:
    if símb == '(':
        lista_abert.append(símb)
    elif símb == ')':
        lista_fech.append(símb)

if len(lista_abert) == len(lista_fech):
    print('A expressão digitada está correta!')
else:
    print('A expressão digitada está incorreta!')
