CREATE TABLE IF NOT EXISTS Tipo (
	Id_tipo INT PRIMARY KEY,
	Tipos VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Banco (
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

CREATE TABLE IF NOT EXISTS Gastos (
	Id_gastos SERIAL PRIMARY KEY,
	Energia NUMERIC(5,2),
	Agua NUMERIC(5,2),
	Condominio NUMERIC(5,2),
	Propaganda NUMERIC(5,2)
);

CREATE TABLE IF NOT EXISTS Pagamento (
	Id_pagamento SERIAL PRIMARY KEY,
	Vista BOOLEAN,
	Id_banco INT,
	Entrada NUMERIC(5,2),
	N_parcelas INT,
	FOREIGN KEY (Id_banco) REFERENCES Banco(Id_banco)	
);

CREATE TABLE IF NOT EXISTS Cliente (
	Id_cliente SERIAL PRIMARY KEY,
	Id_pessoa INT,
	Id_endereco INT,	
	FOREIGN KEY (Id_endereco) REFERENCES Endereco(Id_endereco),
	FOREIGN KEY (Id_pessoa) REFERENCES Pessoa(Id_pessoa)	
);

CREATE TABLE IF NOT EXISTS Imovel (
	Id_imovel SERIAL PRIMARY KEY,
	Id_endereco INT,
	Id_tipo INT,
	Id_gastos INT,
	Idade INT,
	Id_cliente INT,
	FOREIGN KEY (Id_endereco) REFERENCES Endereco(Id_endereco),
	FOREIGN KEY (Id_tipo) REFERENCES Tipo(Id_tipo),
	FOREIGN KEY (Id_gastos) REFERENCES Gastos(Id_gastos),
	FOREIGN KEY (Id_cliente) REFERENCES Cliente(Id_cliente)
);

CREATE TABLE IF NOT EXISTS Transacao (
	Id_transacao SERIAL PRIMARY KEY,
	Id_imovel INT,
	Id_comprador INT,
	Id_proprietario INT,	
	Id_pagamento INT,
	FOREIGN KEY (Id_imovel) REFERENCES Imovel(Id_imovel),
	FOREIGN KEY (Id_comprador) REFERENCES Cliente(Id_cliente),
	FOREIGN KEY (Id_proprietario) REFERENCES Cliente(Id_cliente),
	FOREIGN KEY (Id_pagamento) REFERENCES Pagamento(Id_pagamento)
);

