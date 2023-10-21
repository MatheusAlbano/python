somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho_F = ""
tot_mulher = 0
for i in range(1,5):
    print("\033[m----- {}ª Pessoa -----".format(i))
    nome = input("Nome:\033[32m ").strip()
    idade = int(input("\033[mIdade:\033[32m "))
    sexo = input("\033[mSexo [M/F]:\033[32m ").strip()
    somaidade = somaidade + idade    
    if i == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho_M = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho_M = nome
    if sexo in "Ff" and idade < 20: 
        tot_mulher += 1

mediaidade = somaidade / 4
print("\033[mA média de idade do grupo é de \033[32m{} anos\033[m".format(mediaidade))            
print("\033[mO homem mais velho possui \033[32m{} anos\033[m e se chama \033[32m{}\033[m".format(maioridadehomem,nomevelho_M))   
if 
print("\033[mAo todo são \033[32m{}\033[m mulheres com menos de 20 anos".format(tot_mulher))         


