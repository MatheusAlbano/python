
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
    print(5*"=-==-")
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    opcao = int(input(">>>>> Qual é a sua opção? "))
    if opcao == 1:
        print("A soma entre {} + {} é {}".format(n1,n2,n1+n2))
    elif opcao == 2:
        print("A multiplicação entre {} x {} é {}".format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print("Entre {} e {} o maior é {}".format(n1,n2,n1))    
        elif n1 < n2:
            print("Entre {} e {} o maior é {}".format(n1,n2,n2))   
        else:
            print("Entre {} e {} os dois números são iguais, não existe um maior.".format(n1,n2)) 
    elif opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        print(5*"=-==-")
        print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
        opcao = int(input(">>>>> Qual é a sua opção? ")) 
        if opcao == 1:
            print("A soma entre {} + {} é {}".format(n1,n2,n1+n2))
        elif opcao == 2:
            print("A multiplicação entre {} x {} é {}".format(n1,n2,n1*n2))
        elif opcao == 3:
            if n1 > n2:
                 print("Entre {} e {} o maior é {}".format(n1,n2,n1))    
        elif n1 < n2:
            print("Entre {} e {} o maior é {}".format(n1,n2,n2))   
        else:
            print("Entre {} e {} os dois números são iguais, não existe um maior.".format(n1,n2))
             
print("FIM DO PROGRAMA! VOLTE SEMPRE!")            

