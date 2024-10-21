DROP DATABASE IF EXISTS banco_zl; --caso de erro no banco

CREATE DATABASE banco_zl;
-- Atribuir os privilégios de acesso aos objetos do banco
-- para o usuário root
GRANT ALL PRIVILEGES ON banco.* TO 'root'@'localhost';

-- Acessar o banco de dados: banco
USE banco;

-- Criar a tabela: usuario
CREATE TABLE usuario(
    id INT AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    login VARCHAR(20) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);