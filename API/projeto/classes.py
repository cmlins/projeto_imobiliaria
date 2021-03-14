from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app_ = Api(app=app, version='1.0', title='Imobiliaria', description='Sistema de venda de imóveis')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/Imobiliaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
app.secret_key = "alquimia"
db = SQLAlchemy(app)

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
    nome = db.Column(db.String)
    cpf = db.Column(db.String)
    data_nasc = db.Column(db.Date)
    rg = db.Column(db.String)
    profissao = db.Column(db.String)
    estado_civil = db.Column(db.String)

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

    def __init__(self, id_gastos, energia, agua, condominio, propaganda):
        self.id_gastos = id_gastos
        self.energia = energia
        self.agua = agua
        self.condominio = condominio
        self.propaganda = propaganda

class Pagamento(db.Model):   
    __tablename__ = 'pagamento'
    id_pagamento = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    vista = db.Column(db.Integer)
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id_banco'), nullable=False)
    entrada = db.Column(db.Integer)
    n_parcelas = db.Column(db.Integer)

    def __init__(self, id_pagamento, vista, id_banco, entrada, n_parcelas):
        self.id_pagamento = id_pagamento
        self.vista = vista
        self.id_banco = id_banco
        self.entrada = entrada
        self.n_parcelas = n_parcelas

class Imovel(db.Model):   
    __tablename__ = 'imovel'
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipo.id_tipo'), nullable=False)
    id_gastos = db.Column(db.Integer, db.ForeignKey('tipo.id_gastos'), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def __init__(self, id_endereco, id_tipo):
        self.id_endereco = id_endereco
        self.id_tipo = id_tipo

class Cliente(db.Model):   
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
    id_imovel = db.Column(db.Integer, db.ForeignKey('imovel.id_imovel'))
    
    def __init__(self, id_pessoa, id_endereco, id_imovel):
        self.id_pessoa = id_pessoa
        self.id_endereco = id_endereco
        self.id_imovel = id_imovel

class Transacao(db.Model):
    id_transacao = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True),
    id_comprador = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False),
    id_proprietario = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False),
    id_pagamento = db.Column(db.Integer, db.ForeignKey('pagamento.id_pagamento'), nullable=False)

    def __init__(self, id_comprador, id_proprietario, id_pagamento):
        self.id_comprador = id_comprador
        self.id_proprietario = id_endereco
        self.id_pagamento = id_pagamento

################# VERSION 1.0 ###########################

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
    nome = db.Column(db.String)
    cpf = db.Column(db.String)
    data_nasc = db.Column(db.Date)
    rg = db.Column(db.String)
    profissao = db.Column(db.String)
    estado_civil = db.Column(db.String)

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

    def __init__(self, id_gastos, energia, agua, condominio, propaganda):
        self.id_gastos = id_gastos
        self.energia = energia
        self.agua = agua
        self.condominio = condominio
        self.propaganda = propaganda

class Imovel(db.Model):   
    __tablename__ = 'imovel'
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipo.id_tipo'), nullable=False)
    id_gastos = db.Column(db.Integer, db.ForeignKey('gastos.id_gastos'), nullable=False)

    def __init__(self, id_endereco, id_gastos):
        self.id_endereco = id_endereco
        self.id_tipo = id_tipo
        self.id_gastos = id_gastos

class Proprietario(db.Model):   
    __tablename__ = 'proprietario'
    id_proprietário = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_imovel = db.Column(db.Integer, db.ForeignKey('imovel.id_imovel'), nullable=False)
    tempo_propriedade = db.Column(db.Integer)

    def __init__(self, id_pessoa, id_imovel, id_gastos, tempo_propriedade):
        self.id_pessoa = id_pessoa
        self.id_imovel = id_imovel
        self.tempo_propriedade = tempo_propriedade

class Pagamento(db.Model):   
    __tablename__ = 'pagamento'
    id_pagamento = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    vista = db.Column(db.Integer)
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id_banco'), nullable=False)
    entrada = db.Column(db.Integer)
    n_parcelas = db.Column(db.Integer)

    def __init__(self, id_pagamento, vista, id_banco, entrada, n_parcelas):
        self.id_pagamento = id_pagamento
        self.vista = vista
        self.id_banco = id_banco
        self.entrada = entrada
        self.n_parcelas = n_parcelas

class Cliente(db.Model):   
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
    id_pagamento = db.Column(db.Integer, db.ForeignKey('pagamento.id_pagamento'), nullable=False)

    def __init__(self, id_pessoa, id_endereco, id_pagamento):
        self.id_pessoa = id_pessoa
        self.id_endereco = id_endereco
        self.id_pagamento = id_pagamento

