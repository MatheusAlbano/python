def ficha(nome='', gols=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


#Programa Principal
print('-'*30)
n = input('Nome do Jogador: ')
g = input('Número de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
print(ficha(n,g))