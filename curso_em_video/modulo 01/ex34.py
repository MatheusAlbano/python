salario = float(input("Informe o salário do funcionário: R$"))

if salario > 1250.00:
    salario1 = salario * (110/100)
    print("Salário antigo: R${:.2f}\nSalário atual com aumento de 10%: R${:.2f}".format(salario, salario1))
else:
    salario2 = salario * (115/100)    
    print("Salário antigo: R${:.2f}\nSalário atual com aumento de 15%: R${:.2f}".format(salario, salario2))

