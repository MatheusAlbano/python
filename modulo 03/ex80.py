valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    for c, v in enumerate(valores):
        if v == max(valores):
            valores.insert(c,v)
            print('Adicionado ao final da lista...')
        else:
            
            