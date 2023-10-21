print("--"*8)
print("CALCULADORA IMC")
print("--"*8)

peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso/(altura**2)

if (imc < 18.5):
    print("O seu IMC resultou no valor de {:.2f}, indicando que você está ABAIXO DO PESO.".format(imc))
elif (imc >= 18.5) and (imc <= 25):
    print("O seu IMC resultou no valor de {:.2f}, indicando que você está no PESO IDEAL.".format(imc))  
elif (imc >= 25) and (imc < 30): 
    print("O seu IMC resultou no valor de {:.2f}, indicando que você está com SOBREPESO.".format(imc))
elif (imc >= 30) and (imc < 40):
    print("O seu IMC resultou no valor de {:.2f}, indicando que você está com OBESIDADE.".format(imc))
else: 
    print("O seu IMC resultou no valor de {:.2f}, indicando que você está com OBESIDADE MÓRBIDA.".format(imc))    

