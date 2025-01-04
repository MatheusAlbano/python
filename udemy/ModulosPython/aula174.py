# Maria pegou um empréstimo de 1.000.000
# Para realizar o pagamento em 5 anos
# A data que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela 
# é no dia 20 de cadas mês
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  # Para somar meses corretamente

# Formato de data para exibição
fmt = '%d/%m/%Y'

# Data do início do empréstimo
data_emprestimo = datetime(2020, 12, 20)
data_emprestimo_fmt = data_emprestimo.strftime(fmt)
print(f'DATA INÍCIO: {data_emprestimo_fmt}')

# Data do fim do empréstimo (5 anos depois)
data_final_emprestimo = data_emprestimo + relativedelta(years=5)
data_final_emprestimo_fmt = data_final_emprestimo.strftime(fmt)
print(f'DATA FIM: {data_final_emprestimo_fmt}')

# Valor do empréstimo e da parcela
valor_emprestimo = 1000000
numero_parcelas = 60
valor_parcela = valor_emprestimo / numero_parcelas

# Exibir as datas de vencimento e o valor de cada parcela
print("\nDatas de vencimento e valor das parcelas:")

for i in range(numero_parcelas):
    data_vencimento = data_emprestimo + relativedelta(months=i)
    data_vencimento_fmt = data_vencimento.strftime(fmt)
    print(f'Parcela {i+1}: Vencimento: {data_vencimento_fmt} - Valor: R${valor_parcela:,.2f}')





