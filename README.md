# Insight Places

Repositório local para acompanhamento do projeto de banco de dados `insight_places`.

## Descrição

Este projeto possui um conjunto de tabelas para gerenciamento de proprietários, clientes, hospedagens, alugueis e avaliações. Inclui scripts SQL para criação do banco de dados, bem como planejamento para popular as tabelas com dados de exemplo. Desenvolvido no contexto do curso **Consultas SQL com MySQL Server da Oracle - ONE Alura**.

## Estrutura do Banco

- **proprietarios**: informações dos proprietários das hospedagens.
- **clientes**: cadastro de clientes.
- **enderecos**: endereços das hospedagens.
- **hospedagens**: detalhes das hospedagens disponíveis.
- **alugueis**: registros de aluguel de hospedagens.
- **avaliacoes**: avaliações feitas pelos clientes (opcional).

## Configuração do Ambiente

1. Criar o arquivo `.env` com as credenciais do banco de dados:
    ```env
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=insight_places
    DB_USER=root
    DB_PASSWORD=sua_senha_aqui
    ```

2. Executar o script `create_banco.sql` para criar o banco e suas tabelas.
