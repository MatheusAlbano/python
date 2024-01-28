"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_str = input('Digite um número inteiro: ')
print('-' * 20)

if num_str.isdigit():
    num_int = int(num_str)
    par_impar = num_int % 2 == 0
    par_impar_texto = 'ÍMPAR'

    if par_impar:
        par_impar_texto = 'PAR'
    
    print(f'O número {num_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
   
print('-' * 20)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input('Digite o horário atual em números inteiros: ')
print('-' * 20)

if hora_str.isdigit(): 
    hora_int = int(hora_str)

    if (0 <= hora_int <= 11):
        print('Bom dia!')
    elif (12 <= hora_int <= 17):
        print('Boa tarde!')
    elif (18 <= hora_int <= 23):
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
else:
    print('Você não digitou um horário válido.')

print('-' * 20)


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')
tamanho = len(nome)

print('-' * 20)
if tamanho > 1:
    if tamanho <= 4:
        print('Seu nome é curto')
    elif tamanho <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

print('-' * 20)