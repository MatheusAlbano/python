vel = float(input("Informe a velocidade do carro: "))
if vel > 80:
    multa = (vel - 80) * 7
    print("MULTADO! Você excedeu o limite de velocidade de 80km/h e deverá pagar uma multa de R${:.2f}".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança.")    


