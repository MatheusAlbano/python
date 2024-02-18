# from sys import path
# import aula106_package.modulo
# from aula106_package import modulo
# from aula106_package.modulo import *

# # from aula106_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula106_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula106_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

from aula106_package import falar_oi, soma_do_modulo

print(soma_do_modulo(2, 3))
falar_oi()


