import math

cat_oposto = float(input("Informe o valor da medida do cateto oposto: "))
cat_adj = float(input("Informe o valor da medida do cateto adjascente: "))

print("O triângulo de cateto oposto igual a {} e cateto adjascente igual a {}, possui a medida da hipotenusa igual a {:.2f}".format(cat_oposto, cat_adj, math.hypot(cat_oposto, cat_adj)))