def metade(preço):
    res = preço / 2
    return res

def dobro(preço):
    res =  preço * 2
    return res

def aumentar(preço, porc):
    res =  preço * (100 + porc) / 100
    return res

def diminuir(preço, porc):
    res = preço * (100 - porc) / 100
    return res
