import random

print("--"*4)
print("JOKENPÔ")
print("--"*4)

jogo = ["PAPEL","PEDRA","TESOURA"]

computador = random.choice(jogo)
eu = input("PEDRA, PAPEL OU TESOURA: ")
eu_up = eu.upper()
print("O computador jogou {}".format(computador))
print("O jogador jogou {}".format(eu_up))



if (eu_up == "TESOURA") and (computador == "PAPEL"):
    print("--"*6)
    print("VOCÊ GANHOU")
    print("--"*6)
elif (eu_up == "TESOURA") and (computador == "PEDRA"):
    print("--"*6)
    print("VOCÊ PERDEU")    
    print("--"*6)
elif (eu_up == "PEDRA") and (computador == "PAPEL"):
    print("--"*6)
    print("VOCÊ PERDEU")
    print("--"*6)
elif (eu_up == "PEDRA") and (computador == "TESOURA"):
    print("--"*6)
    print("VOCÊ VENCEU")
    print("--"*6)
elif (eu_up == "PAPEL") and (computador == "TESOURA"):
    print("--"*6)
    print("VOCÊ PERDEU") 
    print("--"*6)
elif (eu_up == "PAPEL") and (computador == "PEDRA"):
    print("--"*6)
    print("VOCÊ VENCEU")
    print("--"*6)
elif (eu_up == computador):
    print("--"*6)
    print("EMPATE")
    print("--"*6)
    jokenpo()
    

