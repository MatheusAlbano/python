cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    if (numero>=0) & (numero<=20):
        print(f'Você digitou o número {cont[numero]}')
        break
    else:
        print('Tente Novamente. ',end='')