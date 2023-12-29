def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade <=65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: NÃO VOTA'

print('-'*30)
a = int(input('Em que ano você nasceu? '))
print(voto(a))





    
    