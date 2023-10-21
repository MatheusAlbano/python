print("--"*12)
print("CONDIÇÕES DE PAGAMENTO")
print("--"*12)
preco_normal = float(input("Valor do produto: R$"))
condicao_pag = int(input("Opções de pagamento: \n1- À vista dinheiro/cheque: 10% de desconto\n2- À vista no cartão: 5% de desconto\n3- Em até 2x no cartão: Preço normal\n4- 3x ou mais no cartão: 20% de juros\nQual a condição de pagamento desejada: "))

if (condicao_pag == 1):
    desc10 = preco_normal - (preco_normal*10/100)
    print("O produto custará à vista no dinheiro/cheque: R${:.2f}".format(desc10))
elif (condicao_pag == 2):
    desc5 = preco_normal - (preco_normal*5/100)
    print("O produto custará à vista no cartão: R${:.2f}".format(desc5))
elif (condicao_pag == 3):
    print("O valor do produto parcelado em até 2x no cartão custará no final: R${:.2f}".format(preco_normal))  
elif (condicao_pag == 4):
    juros20 = preco_normal + (preco_normal*20/100)
    print("O valor do produto parcelado em 3x ou mais no cartão custará no final: R${:.2f}".format(juros20))
else: 
    print("Digite uma opção válida") 
    condicao_pag = int(input("Qual a condição de pagamento desejada: \n1- À vista dinheiro/cheque: 10% de desconto\n2- À vista no cartão: 5% de desconto\n3- Em até 2x no cartão: Preço normal\n4- 3x ou mais no cartão: 20% de juros"))

