# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

from dados import produtos
import copy

novos_produtos = copy.deepcopy(produtos)

for i in range(5):
    aumentar_precos = round(novos_produtos[i]['preco'] * 1.10, 2)
    novos_produtos[i]['preco'] = aumentar_precos

# print(*produtos, sep='\n')
# print()    
# print(*novos_produtos, sep='\n')


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# print(*produtos, sep='\n')
# print()    
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)
### FINAL 

print(*produtos, sep='\n')
print()    
print(*novos_produtos, sep='\n')
print()  
print(*produtos_ordenados_por_nome, sep='\n')
print()    
print(*produtos_ordenados_por_preco, sep='\n')