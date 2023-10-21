n = int(input("Digite um número inteiro: "))
contador = 0


while contador <= n:
    tabuada = n * contador
    print("{} X {} = {}".format(n, contador, tabuada))
    contador += 1