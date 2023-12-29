import random
from time import sleep
num = random.randrange(0,5)
print("-=-" * 17)
print("Vou pensar em número entre 0 e 5. Tente adivinhar...")
print("-=-" * 17)
n = int(input("Em que número eu pensei: "))
print("PROCESSANDO...")
sleep(3)
if n == num:
    print("VOCÊ VENCEU!")
else: 
    print("-=-" * 5)
    print("VOCÊ PERDEU!")
    print("-=-" * 5)
    print("-=-" * 8)
    print("O NÚMERO ESCOLHIDO ERA: {}".format(num))    
    print("-=-" * 8)
