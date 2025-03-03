-- Criando a coluna dos anos
SELECT EXTRACT (YEAR FROM "Data_da_Ocorrencia") AS Ano,
* FROM anac_sqlalchemy;

-- Trazendo os anos distintos
SELECT DISTINCT
EXTRACT (YEAR FROM "Data_da_Ocorrencia") AS Ano
FROM anac_sqlalchemy
ORDER BY Ano

-- Filtrando o ano atual
SELECT EXTRACT (YEAR FROM "Data_da_Ocorrencia") AS Ano,
	   EXTRACT (YEAR FROM CURRENT_DATE) AS Ano_Atual,
	   * FROM anac_sqlalchemy
	   WHERE EXTRACT
	         (YEAR FROM "Data_da_Ocorrencia") = EXTRACT (YEAR FROM CURRENT_DATE)
			 

-- Deletando os dados do ano atual
DELETE FROM anac_sqlalchemy
WHERE EXTRACT (YEAR FROM "Data_da_Ocorrencia") = EXTRACT (YEAR FROM CURRENT_DATE)