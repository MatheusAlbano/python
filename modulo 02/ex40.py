print("--"*9)
print("SITUAÇÃO DO ALUNO")
print("--"*9)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

if (media < 5):
    print("REPROVADO")
elif (media >= 5) and (media < 7):
    print ("RECUPERAÇÃO")
elif (media >= 7):     
    print("APROVADO")        
