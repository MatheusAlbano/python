n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

if (n1 > n2) & (n1 > n3): #CASO O PRIMEIRO NÚMERO SEJA O MAIOR
    print("Maior número: {}".format(n1))
    if n2 > n3: #CASO O PRIMEIRO SEJA O MAIOR E O TERCEIRO SEJA O MENOR
        print("Menor número: {}".format(n3))
    else: #CASO O PRIMEIRO SEJA O MAIOR E O SEGUNDO SEJA O MENOR
        print("Menor número: {}".format(n2))  
if (n2 > n1) & (n2 > n3): #CASO O SEGUNDO NÚMERO SEJA O MAIOR
    print("Maior número: {}".format(n2))
    if n1 < n3: #CASO O SEGUNDO NÚMERO SEJA O MAIOR E O PRIMEIRO SEJA O MENOR
        print("Menor número: {}".format(n1))     
    else: #CASO O SEGUNDO NÚMERO SEJA O MAIOR E O TERCEIRO SEJA O MENOR
        print("Menor número: {}".format(n3))
if (n3 > n1) & (n3 > n2): #CASO O TERCEIRO NÚMERO SEJA O MAIOR
    print("Maior número: {}".format(n3))    
    if n2 > n1: #CASO O TERCEIRO NÚMERO SEJA O MAIOR E O PRIMEIRO SEJA O MENOR
        print("Menor número: {}".format(n1))    
    else: #CASO O TERCEIRO NÚMERO SEJA O MAIOR E O SEGUNDO SEJA O MENOR
        print("Menor número: {}".format(n2))    
if n1 == n2 & n2 == n3: #CASO OS TRÊS NUMEROS SEJAM IGUAIS
    print("Os três números são iguais")  
  

            

