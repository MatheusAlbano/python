km = float(input("Informe a quantidade de quilômetros percorridos pelo carro: "))
dias = int(input("Informe por quantos dias o carro foi alugado: "))
valor = (dias * 60) + (0.15 * km)

print("O valor a ser cobrado de um carro alugado por {} dias e {}km rodados, é de R${:.2f}".format(dias, km, valor))
