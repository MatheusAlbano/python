maior = 0
menor = 0
for i in range(1,6):
    peso = float((input("\033[mPeso da {}ª pessoa: \033[32m".format(i))))
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso        
print("\033[mO maior peso lido foi de \033[32m{}\033[mkg".format(maior))
print("O menor peso lido foi de \033[31m{}\033[mkg".format(menor))            
