import csv

# Nome do arquivo CSV de entrada e do arquivo de saída com os INSERTs
input_file = 'd:\\cursos\\python3\\udemy\\Modulos Python\\municipios.csv'
output_file = 'insert_municipios.sql'

# Nome da tabela no banco de dados
table_name = 'MUNICIPIO'

# Abrir o arquivo CSV e gerar os comandos INSERT
with open(input_file, mode='r', encoding='utf-8') as csvfile, open(output_file, mode='w', encoding='utf-8') as sqlfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        estado_cod = row['COD UF']
        cod = row['COD']
        nome = row['NOME'].replace("'", "''")  # Escapar apóstrofos para SQL
        insert_command = f"INSERT INTO {table_name} (ESTADO_COD, COD, NOME) VALUES ({estado_cod}, {cod}, '{nome}');\n"
        sqlfile.write(insert_command)

print(f"Arquivo '{output_file}' criado com sucesso!")
