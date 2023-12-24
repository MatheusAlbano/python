from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - ano
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['contratação'] + 35 - ano
    
print('-='*30)
print(dados)    
for k, v in dados.items():
    print(f'{k} tem o valor {v}')

    

