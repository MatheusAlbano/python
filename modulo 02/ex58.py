from time import sleep
from random import randint

print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
computador = randint(0,10)
n = int(input("Qual é seu palpite? "))
print("PROCESSANDO...")
sleep(2)
contador = 1

while n != computador:
    if n < computador:
        print("Mais... Tente mais uma vez")
        n = int(input("Qual é seu palpite? "))
        contador += 1
    else:
        print("Menos... Tente mais uma vez.")
        n = int(input("Qual é seu palpite? "))
        contador +=1
print("Acertou com {} tentativas. Parabéns!".format(contador))            
