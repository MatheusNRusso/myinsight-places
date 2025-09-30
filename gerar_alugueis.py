import random
from datetime import datetime, timedelta

NUM_REGISTROS = 1000
CLIENTE_MAX = 1000
HOSPEDAGEM_MAX = 1000

def gerar_data_inicio():
    hoje = datetime.today()
    dias_aleatorios = random.randint(0, 365 * 2)
    return (hoje - timedelta(days=dias_aleatorios)).date()

def gerar_data_fim(data_inicio):
    dias_aluguel = random.randint(1, 15)
    return data_inicio + timedelta(days=dias_aluguel)

def gerar_preco_total():
    return round(random.uniform(100, 2000), 2)

with open("reservas.sql", "w") as f:
    f.write("USE insight_places;\n\n")
    f.write("INSERT INTO reservas (cliente_id, hospedagem_id, data_inicio, data_fim, preco_total, ativo) VALUES\n")

    for i in range(NUM_REGISTROS):
        cliente_id = random.randint(1, CLIENTE_MAX)
        hospedagem_id = random.randint(1, HOSPEDAGEM_MAX)
        data_inicio = gerar_data_inicio()
        data_fim = gerar_data_fim(data_inicio)
        preco_total = gerar_preco_total()
        ativo = random.choice([1,1,1,0])

        linha = f"({cliente_id}, {hospedagem_id}, '{data_inicio}', '{data_fim}', {preco_total}, {ativo})"
        if i < NUM_REGISTROS - 1:
            linha += ",\n"
        else:
            linha += ";\n"

        f.write(linha)

print("Arquivo 'reservas.sql' gerado com sucesso!")
