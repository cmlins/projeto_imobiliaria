CREATE TABLE IF NOT EXISTS Tipo (
	Id_tipo INT PRIMARY KEY,
	Tipos VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Bancos (
	Id_banco Int PRIMARY KEY,
	Nome_banco VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Endereco (
	Id_endereco SERIAL PRIMARY KEY,
	Rua VARCHAR(100),
	Numero VARCHAR(10),
	Andar VARCHAR(10),
	Bloco VARCHAR(10),
	Bairro VARCHAR(100),
	Cep VARCHAR(10),
	Cidade VARCHAR(100),
	Uf VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Pessoa (
	Id_pessoa SERIAL PRIMARY KEY,
	Nome VARCHAR(100) NOT NULL,
	Cpf VARCHAR(11) NOT NULL,
	Data_nasc DATE,
	RG VARCHAR(15),
	Profissao VARCHAR(100),
	Estado_civil VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Gastos_previos (
	Id_gastos SERIAL PRIMARY KEY,
	Energia NUMERIC(5,2),
	Agua NUMERIC(5,2),
	Condominio NUMERIC(5,2),
	Propaganda NUMERIC(5,2)
);

CREATE TABLE IF NOT EXISTS Imovel (
	Id_imovel SERIAL PRIMARY KEY,
	Id_endereco INT,
	Id_tipo INT,
	FOREIGN KEY (Id_endereco) REFERENCES Endereco(Id_endereco),
	FOREIGN KEY (Id_tipo) REFERENCES Tipo(Id_tipo)
);

CREATE TABLE IF NOT EXISTS Proprietario (
	Id_proprietário  SERIAL PRIMARY KEY,
	Id_pessoa INT,
	Id_imovel INT,
	id_gastos INT,	
	Tempo_propriedade NUMERIC(5,2),
	FOREIGN KEY (Id_pessoa) REFERENCES Pessoa(Id_pessoa),
	FOREIGN KEY (Id_imovel) REFERENCES Imovel(Id_imovel),
	FOREIGN KEY (id_gastos) REFERENCES Gastos_previos(id_gastos)
);

CREATE TABLE IF NOT EXISTS Pagamento (
	Id_pagamento SERIAL PRIMARY KEY,
	Vista BOOLEAN,
	Id_banco INT,
	Entrada NUMERIC(5,2),
	N_parcelas INT,
	FOREIGN KEY (Id_banco) REFERENCES Bancos(Id_banco)	
);

CREATE TABLE IF NOT EXISTS Cliente (
	Id_cliente SERIAL PRIMARY KEY,
	Id_pessoa INT,
	Id_endereco INT,
	Id_pagamento INT,	
	FOREIGN KEY (Id_endereco) REFERENCES Endereco(Id_endereco),
	FOREIGN KEY (Id_pessoa) REFERENCES Pessoa(Id_pessoa),
	FOREIGN KEY (Id_pagamento) REFERENCES Pagamento(Id_pagamento),
);


