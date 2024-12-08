import os 
from itertools import count

caminho = os.path.join('C:', 'Users', 'mathe', 'Testando os.walk')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(' ', the_counter, 'Pasta Atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'Dir: ', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        print(' ', the_counter, "File: ", caminho_completo)