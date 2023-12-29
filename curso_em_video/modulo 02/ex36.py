print("-=-"*18)
print("Análise Empréstimo Bancário para compra de uma casa")
print("-=-"*18)

valor_casa = float(input("Qual o valor da casa desejada: R$"))
salario = float(input("Informe o salário mensal do comprador: R$"))
periodo = int(input("Em quantos anos deseja quitar o imóvel: "))

parcelas =  periodo*12
prestacao = (valor_casa/parcelas)

if (prestacao <= salario*30/100):
    print("EMPRÉSTIMO APROVADO, PARABÉNS!")
    print("O VALOR SERÁ DIVIDIDO EM {}x PARCELAS MENSAIS DE R${:.2f} CADA.".format(parcelas,prestacao))
else: 
    print("EMPRÉSTIMO REPROVADO, A ANÁLISE CONSTATOU QUE O SEU SALÁRIO NÃO É COMPÁTIVEL COM O VALOR DO IMÓVEL E O PERIÓDO QUE DESEJA QUITÁ-LO.")    

