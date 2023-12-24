dados = dict()
ficha = list()
som_idade = som_mulheres =  0
while True:
    dados.clear()
    dados['nome'] = input('Nome: ')
    while True:
        dados['sexo'] = input('Sexo: [M/F] ').strip().upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.') 
    dados['idade'] = int(input('Idade: '))
    som_idade += dados['idade']
    ficha.append(dados.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(ficha)} pessoas cadastradas.')
print(f'B) A média de idade é de {som_idade/len(ficha):.2f} anos')
print(f'C) As mulheres cadastradas foram ',end='')
for p in ficha:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}... ',end='')
print()
print('D) A lista das pessoas que estão acima da média: ')
for p in ficha:
    if p['idade'] >= som_idade/len(ficha):
        print('    ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<< ENCERRADO >>>')





