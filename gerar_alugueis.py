import random
from datetime import datetime, timedelta

NUM_REGISTROS = 1000
CLIENTE_MAX = 1000
HOSPEDAGEM_MAX = 1000

# Função para gerar uma data aleatória nos últimos 2 anos
def gerar_data_inicio():
    hoje = datetime.today()
    dias_aleatorios = random.randint(0, 365 * 2)  # últimos 2 anos
    data_inicio = hoje - timedelta(days=dias_aleatorios)
    return data_inicio.date()

# Função para gerar data de fim (1 a 15 dias após o início)
def gerar_data_fim(data_inicio):
    dias_aluguel = random.randint(1, 15)
    data_fim = data_inicio + timedelta(days=dias_aluguel)
    return data_fim

# Função para gerar preço total entre 100 e 2000
def gerar_preco_total():
    return round(random.uniform(100, 2000), 2)

with open("inserts_alugueis.sql", "w") as f:
    f.write("INSERT INTO alugueis (cliente_id, hospedagem_id, data_inicio, data_fim, preco_total) VALUES\n")

    for i in range(NUM_REGISTROS):
        cliente_id = random.randint(1, CLIENTE_MAX)
        hospedagem_id = random.randint(1, HOSPEDAGEM_MAX)
        data_inicio = gerar_data_inicio()
        data_fim = gerar_data_fim(data_inicio)
        preco_total = gerar_preco_total()

        linha = f"({cliente_id}, {hospedagem_id}, '{data_inicio}', '{data_fim}', {preco_total})"
        if i < NUM_REGISTROS - 1:
            linha += ",\n"
        else:
            linha += ";\n"

        f.write(linha)

print("Arquivo inserts_alugueis.sql gerado com sucesso!")
