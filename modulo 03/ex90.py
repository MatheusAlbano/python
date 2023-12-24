aluno = dict()
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] < 5: 
    aluno['situação'] = 'Reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print(f'Situação é igual a {aluno["situação"]}')
