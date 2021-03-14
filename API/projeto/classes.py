class Tipo(db.Model):   
    __tablename__ = 'tipo'
    id_tipo = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    tipo = db.Column(db.String)
    
    def __init__(self, tipo):
        self.tipo = tipo

class Banco(db.Model):   
    __tablename__ = 'banco'
    id_banco = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nome_banco = db.Column(db.String)
    
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

class Endereco(db.Model):   
    __tablename__ = 'endereco'
    id_endereco = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    rua = db.Column(db.String)
    numero = db.Column(db.String)
    andar = db.Column(db.String)
    bloco = db.Column(db.String)
    bairro = db.Column(db.String)
    cep = db.Column(db.String)
    cidade = db.Column(db.String)
    uf = db.Column(db.String)

    def __init__(self, rua, numero, andar, bloco, bairro, cep, cidade, uf):
        self.rua = rua
        self.numero = numero
        self.andar = andar
        self.bloco = bloco
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

class Pessoa(db.Model):   
    __tablename__ = 'pessoa'
    id_pessoa = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable=False)
    data_nasc = db.Column(db.String, nullable=False)
    rg = db.Column(db.String, nullable=False)
    profissao = db.Column(db.String, nullable=False)
    estado_civil = db.Column(db.String, nullable=False)

    def __init__(self, nome, cpf, data_nasc, rg, profissao, estado_civil):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.rg = rg
        self.profissao = profissao
        self.estado_civil = estado_civil

class Gastos(db.Model):   
    __tablename__ = 'gastos'
    id_gastos = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    energia = db.Column(db.Integer)
    agua = db.Column(db.Integer)
    condominio = db.Column(db.Integer)
    propaganda = db.Column(db.Integer)

    def __init__(self, energia, agua, condominio, propaganda):
        self.energia = energia
        self.agua = agua
        self.condominio = condominio
        self.propaganda = propaganda

class Pagamento(db.Model):   
    __tablename__ = 'pagamento'
    id_pagamento = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    vista = db.Column(db.Integer)
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id_banco'))
    entrada = db.Column(db.Integer)
    n_parcelas = db.Column(db.Integer)

    def __init__(self, vista, id_banco, entrada, n_parcelas):
        self.vista = vista
        self.id_banco = id_banco
        self.entrada = entrada
        self.n_parcelas = n_parcelas

class Cliente(db.Model):   
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
    
    def __init__(self, id_pessoa, id_endereco):
        self.id_pessoa = id_pessoa
        self.id_endereco = id_endereco

class Imovel(db.Model):   
    __tablename__ = 'imovel'
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipo.id_tipo'), nullable=False)
    id_gastos = db.Column(db.Integer, db.ForeignKey('gastos.id_gastos'), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)

    def __init__(self, id_endereco, id_tipo, id_gastos, idade, id_cliente):
        self.id_endereco = id_endereco
        self.id_tipo = id_tipo
        self.id_gastos = id_gastos
        self.idade = idade
        self.id_cliente = id_cliente

class Transacao(db.Model):
    __tablename__ = 'transacao'
    id_transacao = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_comprador = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_proprietario = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_pagamento = db.Column(db.Integer, db.ForeignKey('pagamento.id_pagamento'), nullable=False)
    id_imovel = db.Column(db.Integer, db.ForeignKey('imovel.id_imovel'), nullable=False)

    def __init__(self, id_imovel, id_comprador, id_proprietario, id_pagamento):
        self.id_comprador = id_comprador
        self.id_proprietario = id_proprietario
        self.id_pagamento = id_pagamento
        self.id_imovel = id_imovel