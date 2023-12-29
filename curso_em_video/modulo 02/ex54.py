from datetime import date
tot_maior = 0
tot_menor = 0
for i in range(1,8):
    ano = int(input("\033[mEm que ano a {}ª pessoa nasceu: \033[32m".format(i))) 
    idade = date.today().year - ano
    if idade >= 21:
        tot_maior += 1
    else: 
        tot_menor += 1    
print("\033[mAo todo temos {} pessoas maiores de idade".format(tot_maior))
print("E também tivemos {} pessoas menores de idade".format(tot_menor)) 


