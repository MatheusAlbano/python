import importlib

import aula105_m

print(aula105_m.variavel)

for i in range(10):
    importlib.reload(aula105_m)
    print(i)
    

print('Fim')