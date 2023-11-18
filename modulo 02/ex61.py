a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
c = 1
while c <= 10:
    a = a1 + (c-1)*r
    print('{}'.format(a),end='')
    print(' -> ' if c < 10 else ' -> FIM',end='' )
    c += 1