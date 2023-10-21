from datetime import date
print("--"*9)
print("TORNEIO DE NATAÇÃO")
print("--"*9)
ano = int(input("Informe o ano de nascimento do atleta: "))
idade = date.today().year - ano

if (idade <= 9):
    print("CATEGORIA MIRIM")
elif (idade > 9) and (idade <= 14):
    print("CATEGORIA INFANTIL")
elif (idade > 14) and (idade <= 19):
    print("CATEGORIA JUNIOR")
elif (idade > 19) and (idade <= 20):
    print("CATEGORIA SÊNIOR")
else:
    print("CATEGORIA MASTER")         
          
