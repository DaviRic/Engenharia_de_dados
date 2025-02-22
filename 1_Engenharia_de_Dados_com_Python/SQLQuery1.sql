USE Python

CREATE TABLE Minha_Tabela(
	coluna_1 NVARCHAR (20),
	coluna_2 INT,
	coluna_3 MONEY
)

SELECT * FROM Minha_Tabela;

INSERT INTO Minha_Tabela (coluna_1, coluna_2, coluna_3) VALUES ('Davi', 26,	50000);

DELETE FROM Minha_Tabela;

TRUNCATE TABLE Minha_Tabela;