n = int(input("Digite um número inteiro: "))
d = n*2
t = n*3
raiz = n**(1/2)

if(n < 0):
    print("O dobro do número informado é {}, o triplo é igual a {}, e a raiz quadrada desse número não existe".format(d, t))
else:    
    print("O dobro do número informado é {}, o triplo é igual a {}, e a raiz quadrada desse número é {}".format(d, t, raiz))