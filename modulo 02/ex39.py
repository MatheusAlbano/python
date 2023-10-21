from datetime import date
print("---"*11)
print("Situação do Alistamento Militar")
print("---"*11)

ano = int(input("Informe o ano de nascimento do cidadão: "))
ano_atual = date.today().year 
idade = ano_atual - ano

if (idade < 18):
    antes_prazo = 18 - idade
    if(antes_prazo > 1):
        print("O prazo para se alistar ainda não chegou, faltam {} anos para o alistamento.".format(antes_prazo))
    else:
        print("O prazo para se alistar ainda não chegou, falta {} ano para o alistamento.".format(antes_prazo))
elif (idade == 18): 
    print("Está na hora de se alistar!")
elif (idade > 18):
    passou_prazo = idade - 18 
    if(passou_prazo > 1):
        print("Já passou do prazo de alistamento há {} anos.".format(passou_prazo))    
    else:
        print("Já passou do prazo de alistamento há {} ano.".format(passou_prazo))    