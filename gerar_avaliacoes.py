from faker import Faker
import random

fake = Faker('pt_BR')

num_registros = 1000
arquivo_sql = "avaliacoes.sql"

with open(arquivo_sql, "w", encoding="utf-8") as f:
    f.write("USE insight_places;\n\n")
    f.write("INSERT INTO avaliacoes (cliente_id, hospedagem_id, nota, comentario) VALUES\n")

    for i in range(1, num_registros + 1):
        cliente_id = random.randint(1, 1000)  # supondo que você tenha 1000 clientes
        hospedagem_id = random.randint(1, 1000)  # supondo que tenha 1000 hospedagens
        nota = random.randint(1, 5)  # NOT NULL → sempre entre 1 e 5
        comentario = random.choice([fake.sentence(nb_words=10).replace("'", "''"), None])  # pode ser NULL

        comentario_sql = "NULL" if comentario is None else f"'{comentario}'"

        if i == num_registros:
            f.write(f"({cliente_id}, {hospedagem_id}, {nota}, {comentario_sql});\n")
        else:
            f.write(f"({cliente_id}, {hospedagem_id}, {nota}, {comentario_sql}),\n")

print(f"Arquivo '{arquivo_sql}' gerado com {num_registros} registros com sucesso!")
