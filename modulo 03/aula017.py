lanche = ['Hambúrguer','Suco','Pizza','Pudim']
#LISTAS SÃO MUTÁVEIS

lanche[3] = 'Picolé' #Exlui o Pudim e adiciona Picolé no lugar

lanche.append('Pudim') #Adiciona Pudim na última posição da lista

lanche.insert(3,'Refrigerante') #Inclui o elemento Refrigerante na 3ª posição da lista

lanche.pop() #Exlui o último elemento da lista
#lanche.remove('Pudim')
#lanche.del()

lanche.pop(3) #Exclui o elemento que está na 3ª posição 

if 'Açaí' in lanche: #Procura o elemento Açaí dentro da lista
    lanche.remove('Açaí') #Caso tenha esse elemento na lista, o mesmo é exlcuído
else:
    print('Não encontrei Açaí na lista.') #Caso não exista esse elemento na lista, é exibida essa frase

print(lanche)
print(f'Essa lista tem {len(lanche)} elementos.')