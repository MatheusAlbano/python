import csv

input_file = r'd:\cursos\python3\udemy\Modulos Python\municipios.csv'
output_file = r'd:\cursos\python3\udemy\Modulos Python\insert_municipios.sql'
table_name = 'MUNICIPIO'

# Lista para armazenar códigos já inseridos
existing_codes = set()

try:
    with open(input_file, mode='r', encoding='utf-8') as csvfile, open(output_file, mode='w', encoding='utf-8') as sqlfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            estado_cod = row['COD UF']
            cod = row['COD']
            nome = row['NOME'].replace("'", "''")
            
            # Verifica se o código já foi inserido
            if cod not in existing_codes:
                insert_command = f"INSERT INTO {table_name} (ESTADO_COD, COD, NOME) VALUES ({estado_cod}, {cod}, '{nome}');\n"
                sqlfile.write(insert_command)
                existing_codes.add(cod)
except FileNotFoundError:
    print(f"Erro: Arquivo '{input_file}' não encontrado.")
