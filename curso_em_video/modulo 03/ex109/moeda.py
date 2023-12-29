def metade(preço,form=False):
    res = preço / 2
    return res if form is False else moeda(res) 

def dobro(preço,form=False):
    res = preço * 2
    return res if form is False else moeda(res) 

def aumentar(preço, porc,form=False):
    res = preço * (100 + porc) / 100
    return res if form is False else moeda(res) 

def diminuir(preço, porc,form=False):
    res = preço * (100 - porc) / 100
    return res if form is False else moeda(res) 

def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')