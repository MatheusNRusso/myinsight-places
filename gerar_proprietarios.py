from faker import Faker

fake = Faker('pt_BR')  # Para gerar dados brasileiros

num_registros = 1000
arquivo_sql = "proprietarios.sql"

with open(arquivo_sql, "w", encoding="utf-8") as f:
    f.write("USE insight_places;\n\n")
    f.write("INSERT INTO proprietarios (nome, cpf_cnpj, contato) VALUES\n")

    for i in range(1, num_registros + 1):
        nome = fake.name().replace("'", "''")  # Evita problemas com aspas
        # Alterna entre gerar CPF e CNPJ
        if i % 5 == 0:
            cpf_cnpj = fake.cnpj()
        else:
            cpf_cnpj = fake.cpf()
        contato = fake.email()

        # Se for o último registro, fecha com ponto e vírgula
        if i == num_registros:
            f.write(f"('{nome}', '{cpf_cnpj}', '{contato}');\n")
        else:
            f.write(f"('{nome}', '{cpf_cnpj}', '{contato}'),\n")

print(f"Arquivo '{arquivo_sql}' gerado com {num_registros} registros com sucesso!")
