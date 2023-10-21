import math

ang = float(input("Digite a medida do ângulo: "))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print("O seno do ângulo digitado é igual a: {:.2f}\nO cosseno é igual a: {:.2f}\nA tangente é igual a: {:.2f}".format(seno, cos, tan))