print("--"*12)
print("ANALISADOR DE TRIÂNGULOS")
print("--"*12)
r1 = float(input("Comprimento da reta 1: "))
r2 = float(input("Comprimento da reta 2: "))
r3 = float(input("Comprimento da reta 3: "))

if (r1 < r2 + r3) & (r2 < r1 + r3) & (r3 < r1 + r2):
    print("Essas retas formam um triângulo!")
else:
    print("Essas retas não formam um triângulo!") 

if (r1 == r2 == r3):
    print("Esse triângulo é equilátero")
elif (r1 == r2 != r3) or (r2 == r3 != r1) or (r1 == r3 != r2):
    print("Esse triângulo é isósceles")
elif (r1 != r2 != r3):
    print("Esse triângulo é escaleno")       
