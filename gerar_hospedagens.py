from faker import Faker
import random

fake = Faker('pt_BR')

num_registros = 1000
arquivo_sql = "hospedagens.sql"

# Considerando que os endereços e proprietários têm IDs de 1 a 1000
max_endereco_id = 1000
max_proprietario_id = 1000

with open(arquivo_sql, "w", encoding="utf-8") as f:
    f.write("USE insight_places;\n\n")

    # Reiniciar o AUTO_INCREMENT para começar em 1
    f.write("ALTER TABLE hospedagens AUTO_INCREMENT = 1;\n\n")

    f.write("INSERT INTO hospedagens (tipo, endereco_id, proprietario_id, ativo) VALUES\n")

    for i in range(1, num_registros + 1):
        tipo = random.choice(['Apartamento', 'Casa', 'Flat', 'Pousada', 'Chalé']).replace("'", "''")
        endereco_id = random.randint(1, max_endereco_id)
        proprietario_id = random.randint(1, max_proprietario_id)
        ativo = random.choice([1, 1, 1, 0])  # Mais chances de ativo

        if i == num_registros:
            f.write(f"('{tipo}', {endereco_id}, {proprietario_id}, {ativo});\n")
        else:
            f.write(f"('{tipo}', {endereco_id}, {proprietario_id}, {ativo}),\n")

print(f"Arquivo '{arquivo_sql}' gerado com {num_registros} registros com sucesso!")
