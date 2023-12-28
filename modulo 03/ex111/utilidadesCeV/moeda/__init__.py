def metade(preço,form=False):
    res = preço / 2
    return res if form is False else moeda(res) 

def dobro(preço,form=False):
    res = preço * 2
    return res if form is False else moeda(res) 

def aumentar(preço, porc,form=False):
    """
    -> Calcula o aumento de um determinado preço
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param porc: qual é a porcentagem do aumento.
    :param form: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formatação.
    """
    res = preço * (100 + porc) / 100
    return res if form is False else moeda(res) 

def diminuir(preço, porc,form=False):
    res = preço * (100 - porc) / 100
    return res if form is False else moeda(res) 

def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0,aum=10,red=5):
    msg = 'RESUMO DO VALOR'
    print('-'*35)
    print(f'{msg:^35}')
    print('-'*35)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{aum}% de aumento: \t{aumentar(preço,aum,True)}')
    print(f'{red}% de redução: \t{diminuir(preço,red,True)}')
    print('-'*35)