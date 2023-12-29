a1 = float(input("Digite o valor do primeiro termo da P.A: "))
r = float(input("Digite o valor da razão da P.A: "))

for c in range(1,11):
    a = a1 + (c-1)*r
    print ("A{} = {:.1f}".format(c,a))


