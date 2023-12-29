nome = input("Digite o seu nome completo: ").strip()
nomesplit = nome.split()
print("O seu primeiro nome é: {}".format(nomesplit[0]))
i = len(nomesplit) - 1
print("O seu ultimo nome é: {}".format(nomesplit[i]))