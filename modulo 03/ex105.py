def notas(* notas, sit=False):
    """
    notas(* notas, sit=False)
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-'*30)
    analise = dict()
    analise['total'] = len(notas)
    analise['maior'] = max(notas)
    analise['menor'] = min(notas)
    analise['média'] = sum(notas)/len(notas)
    if sit == True:
        if analise['média'] >= 7:
            analise['situação'] = 'BOA'
        elif analise['média'] >= 5:
            analise['situação'] = 'RAZOÁVEL'
        else:
            analise['situação'] = 'RUIM'              
        
    return analise


#Main
resp = notas(5.5, 10, 5, 6.5, sit=True)
print(resp)
