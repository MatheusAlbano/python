import os

lista_compras = list()

while True:
    opcao = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if opcao == 'i':
        os.system('cls')
        inserir = input('Valor: ').capitalize()
        lista_compras.append(inserir)

    elif opcao == 'a':
        apagar_indice = input('Escolha o índice para apagar: ')
        
        try:
            int_apagar_indice = int(apagar_indice)
            del lista_compras[int_apagar_indice]
            print(lista_compras)
        except (ValueError, IndexError):
            print('Não foi possível apagar este índice')
            continue

    elif opcao == 'l':
        if not lista_compras:
            print('Nada para listar')
            continue
            
        else:
            print('-'*15)
            for i, n in enumerate(lista_compras):
                print(i, n)
            print('-'*15)
            

    elif opcao == 's':
        break

    else:
        print('Essa opção é inválida.')


    
    
    

