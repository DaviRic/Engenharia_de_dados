-- Criando banco de dados
CREATE DATABASE IF NOT EXISTS python;

-- Criando tabela via script
CREATE TABLE IF NOT EXISTS python.testepython(
	id INT,
    nome VARCHAR (60)
);

-- Verificando se a tabela foi criada
SELECT * FROM python.testepython;

-- Inserindo dados
INSERT INTO python.testepython (id, nome) VALUES (1, "Edmilson");

-- Verificando dados inseridos
SELECT * FROM python.testepython;

-- Limpando dados
SET SQL_SAFE_UPDATES = 0;
DELETE FROM python.testepython WHERE nome = "Edmilson";

/*
Quando o modo de atualização segura está ativado, o MySQL exige que se use uma cláusula
WHERE que inclua uma chave de índice ao executar operações de modificação de dados como
UPDATE ou DELETE. Essa medida é para garantir que você não atualize ou exclua todas as
linhas em uma tabela sem a devida intensão.
*/

-- Apagando tabela
DROP TABLE python.testepython;

USE python;

-- Criando tabela via script
CREATE TABLE IF NOT EXISTS testepython2(
	id INT, 
    nome VARCHAR(60)
	);

-- Verificando se a tabela foi criada
SELECT * FROM testepython2;

-- Apagando a tabela
DROP TABLE testepython2;

-- Apagando o banco de dados
DROP DATABASE python;

