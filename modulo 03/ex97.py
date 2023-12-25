def escreva(txt):
    tam = len(txt) + 5
    print('~'*tam)
    print(f'{txt:^{tam}}')
    print('~'*tam)

escreva('OLÁ MUNDO!')
escreva('APRENDA PYTHON COM GUSTAVO GUANABARA')
escreva('CEV')
    