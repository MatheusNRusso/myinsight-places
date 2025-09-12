USE insight_places;

CREATE TABLE proprietarios (
    proprietario_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf_cnpj VARCHAR(20) NOT NULL,
    contato VARCHAR(255) NOT NULL
);

CREATE TABLE clientes (
    cliente_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    contato VARCHAR(255) NOT NULL
);

CREATE TABLE enderecos (
    endereco_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    rua VARCHAR(255),              -- Opcional
    numero INT,                    -- Opcional
    bairro VARCHAR(255),           -- Opcional
    cidade VARCHAR(255) NOT NULL,
    estado CHAR(2) NOT NULL,
    cep VARCHAR(10) NOT NULL
);

CREATE TABLE hospedagens (
    hospedagem_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    endereco_id INT NOT NULL,
    proprietario_id INT NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (endereco_id) REFERENCES enderecos(endereco_id) ON DELETE CASCADE,
    FOREIGN KEY (proprietario_id) REFERENCES proprietarios(proprietario_id) ON DELETE CASCADE
);

CREATE TABLE alugueis (
    aluguel_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    hospedagem_id INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE,
    preco_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id) ON DELETE CASCADE,
    FOREIGN KEY (hospedagem_id) REFERENCES hospedagens(hospedagem_id) ON DELETE CASCADE
);

CREATE TABLE avaliacoes (
    avaliacao_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    hospedagem_id INT NOT NULL,
    nota INT,                      -- Opcional
    comentario TEXT,               -- Opcional
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id) ON DELETE CASCADE,
    FOREIGN KEY (hospedagem_id) REFERENCES hospedagens(hospedagem_id) ON DELETE CASCADE
);
