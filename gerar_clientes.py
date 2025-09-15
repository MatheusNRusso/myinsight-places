from faker import Faker

fake = Faker('pt_BR')  # Gera nomes e CPFs brasileiros

num_registros = 1000
arquivo_sql = "clientes.sql"

with open(arquivo_sql, "w", encoding="utf-8") as f:
    f.write("USE insight_places;\n\n")
    f.write("INSERT INTO clientes (nome, cpf, contato) VALUES\n")

    for i in range(1, num_registros + 1):
        nome = fake.name().replace("'", "''")  # Evita erros com aspas simples
        cpf = fake.cpf()
        contato = fake.email()
        
        # Se for o último registro, fecha com ponto e vírgula
        if i == num_registros:
            f.write(f"('{nome}', '{cpf}', '{contato}');\n")
        else:
            f.write(f"('{nome}', '{cpf}', '{contato}'),\n")

print(f"Arquivo '{arquivo_sql}' gerado com {num_registros} registros com sucesso!")
# Script para gerar um arquivo SQL com 1000 registros de clientes fictícios