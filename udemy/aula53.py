"""
Exercício
Exiba os índices de lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
indices = 0
lista.append('João')
lista.append('Matheus')

for nome in lista:
        print(indices, nome, type(nome))
        indices += 1