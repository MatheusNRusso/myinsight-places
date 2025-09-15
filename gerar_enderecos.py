from faker import Faker
import random

fake = Faker('pt_BR')

num_registros = 1000
arquivo_sql = "enderecos.sql"

with open(arquivo_sql, "w", encoding="utf-8") as f:
    f.write("USE insight_places;\n\n")
    f.write("INSERT INTO enderecos (rua, numero, bairro, cidade, estado, cep) VALUES\n")

    for i in range(1, num_registros + 1):
        rua = fake.street_name().replace("'", "''")  # NOT NULL → sempre preenchido
        numero = random.choice([random.randint(1, 9999), None])  # Pode ser NULL
        bairro = random.choice([fake.bairro().replace("'", "''"), None])  # Pode ser NULL
        cidade = fake.city().replace("'", "''")  # NOT NULL
        estado = fake.estado_sigla()  # NOT NULL
        cep = fake.postcode().replace("-", "")  # NOT NULL, sem hífen

        numero_sql = "NULL" if numero is None else str(numero)
        bairro_sql = "NULL" if bairro is None else f"'{bairro}'"

        # Última linha termina com ponto e vírgula
        if i == num_registros:
            f.write(f"('{rua}', {numero_sql}, {bairro_sql}, '{cidade}', '{estado}', '{cep}');\n")
        else:
            f.write(f"('{rua}', {numero_sql}, {bairro_sql}, '{cidade}', '{estado}', '{cep}'),\n")

print(f"Arquivo '{arquivo_sql}' gerado com {num_registros} registros com sucesso!")
