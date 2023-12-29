km = int(input("Informe a distância da viagem em Km: "))
if km <= 200:
    preço1 = 0.50 * km
    print("A passagem para essa viagem custará R${:.2f}".format(preço1))
else:
    preço2 = 0.45 * km
    print("A passagem para essa viagem custará R${:.2f}".format(preço2))    