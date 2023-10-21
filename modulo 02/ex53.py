frase = str(input("\033[mDigite uma frase: ")).strip().upper()
palavras = frase.split()
frase_trat = "".join(palavras)
inverso = ""

for letra in range(len(frase_trat) - 1, -1, -1):
    inverso += frase_trat[letra]
print("O inverso de {} é {}".format(frase_trat,inverso))
if frase_trat == inverso:
    print("A frase é um \033[32mPALÍNDROMO\033[m")
else:
    print("A frase não é um \033[31mPALÍNDROMO\033[m")    
