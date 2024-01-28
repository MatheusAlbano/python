"""
Iterando strings com while
"""
#       012345678910
nome = 'Matheus' # Iteráveis

nova_string = ''
index_nome = 0

while index_nome <= len(nome) - 1:
    nova_string += f'*{nome[index_nome]}'
    index_nome += 1
print(nova_string)
