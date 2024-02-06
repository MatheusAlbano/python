# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

def par_impar(num):
    par = f'O número {num} é PAR'
    impar = f'O número {num} é ÍMPAR'
    if num % 2 == 0:
        return par 
    return impar
        
print(multiplicar(2, 3, 7, 6))
print(par_impar(15))