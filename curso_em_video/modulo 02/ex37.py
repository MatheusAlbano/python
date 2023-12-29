n = int(input("Informe um numero inteiro positivo: "))

baseconvert = int(input("Qual a base de conversão que deseja utilizar: \n1- Binário;\n2- Octal;\n3- Hexadecimal\nDigite o número correspondente a opção desejada: "))

if (baseconvert == 1):
    binario = int(bin(n)[2:])
    print("O número inteiro digitado equivale ao número {} em binário".format(binario))
elif (baseconvert == 2):
    octal = int(oct(n)[2:])
    print("O número inteiro digitado equivale ao número {} em octal".format(octal))
elif (baseconvert == 3):
    hexa = int(hex(n)[2:])
    print("O número inteiro digitado equivale ao número {} em hexadecimal".format(hexa)) 
else:
    print("Digite um número que esteja entre as opções")    
    baseconvert = int(input("Qual a base de conversão que deseja utilizar: \n1- Binário;\n2- Octal;\n3- Hexadecimal\nDigite o número correspondente a opção desejada: "))

