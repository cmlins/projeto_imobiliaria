'''
Desenvolvedora: Cinthya Moreira Lins
cinthyalins@gmail.com
github: cmlins
'''

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app_ = Api(app=app, version='1.0', title='Imobiliaria', description='Sistema de venda de imóveis')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/Imobiliaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
app.secret_key = "alquimia"
db = SQLAlchemy(app)

########### ÁREAS DO SWAGGER ###########

cliente = app_.namespace('Cliente', descrition='Cliente')
transacoes = app_.namespace('Transações', descrition='Transações')
imoveis = app_.namespace('Imóveis', descrition='Imóveis')

########### CLASSES PARA A CRIAÇÃO DAS TABELAS ###########

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
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id_banco'), nullable=False)
    entrada = db.Column(db.Integer)
    n_parcelas = db.Column(db.Integer)

    def __init__(self, vista, id_banco, entrada, n_parcelas):
        self.vista = vista
        self.id_banco = id_banco
        self.entrada = entrada
        self.n_parcelas = n_parcelas

class Imovel(db.Model):   
    __tablename__ = 'imovel'
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipo.id_tipo'), nullable=False)
    id_gastos = db.Column(db.Integer, db.ForeignKey('gastos.id_gastos'), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def __init__(self, id_endereco, id_tipo, id_gastos, idade):
        self.id_endereco = id_endereco
        self.id_tipo = id_tipo
        self.id_gastos = id_gastos
        self.idade = idade

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
    __tablename__ = 'transacao'
    id_transacao = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    id_comprador = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_proprietario = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    id_pagamento = db.Column(db.Integer, db.ForeignKey('pagamento.id_pagamento'), nullable=False)

    def __init__(self, id_comprador, id_proprietario, id_pagamento):
        self.id_comprador = id_comprador
        self.id_proprietario = id_endereco
        self.id_pagamento = id_pagamento

########### MODELOS PARA O SWAGGER ###########

model_end = app_.model('Endereco model', {
    'id_endereco': fields.Integer(required=True, description='id', help='Preenchimento obrigatório'),
    'rua': fields.String(required=True, description='rua', help='Preenchimento obrigatório'),
    'numero': fields.String(required=True, description='numero', help='Preenchimento obrigatório'),
    'andar': fields.String(required=True, description='andar', help='Preenchimento obrigatório'),
    'bloco': fields.String(required=True, description='bloco', help='Preenchimento obrigatório'),
    'bairro': fields.String(required=True, description='bairro', help='Preenchimento obrigatório'),
    'cep': fields.String(required=True, description='cep', help='Preenchimento obrigatório'),
    'cidade': fields.String(required=True, description='cidade', help='Preenchimento obrigatório'),
    'uf': fields.String(required=True, description='uf', help='Preenchimento obrigatório')
})

model_pessoa = app_.model('Pessoa model', {
    'id_pessoa': fields.Integer(required=True, description='id_pessoa', help='Preenchimento obrigatório'),
    'nome': fields.String(required=True, description='nome', help='Preenchimento obrigatório'),
    'cpf': fields.String(required=True, description='cpf', help='Preenchimento obrigatório'),
    'data_nasc': fields.String(required=True, description='data_nasc', help='Preenchimento obrigatório'),
    'rg': fields.String(required=True, description='rg', help='Preenchimento obrigatório'),
    'profissao': fields.String(required=True, description='profissao', help='Preenchimento obrigatório'),
    'estado_civil': fields.String(required=True, description='estado_civil', help='Preenchimento obrigatório')
})

model_gastos = app_.model('Gastos model', {
    'id_gastos': fields.Integer(required=True, description='id_gastos', help='Preenchimento obrigatório'),
    'energia': fields.Integer(required=True, description='energia', help='Preenchimento obrigatório'),
    'agua': fields.Integer(required=True, description='agua', help='Preenchimento obrigatório'),
    'condominio': fields.Integer(required=True, description='condominio', help='Preenchimento obrigatório'),
    'propaganda': fields.Integer(required=True, description='propaganda', help='Preenchimento obrigatório'),
})

model_pagamento = app_.model('Pagamento model', {
    'id_pagamento': fields.Integer(required=True, description='id_pagamento', help='Preenchimento obrigatório'),
    'vista': fields.Boolean(required=True, description='vista', help='Preenchimento obrigatório'),
    'id_banco': fields.Integer(required=True, description='id_banco', help='Preenchimento obrigatório'),
    'entrada': fields.Integer(required=True, description='entrada', help='Preenchimento obrigatório'),
    'n_parcelas': fields.Integer(required=True, description='n_parcelas', help='Preenchimento obrigatório')
})

model_imovel = app_.model('Imovel model', {
    'id': fields.Integer(required=True, description='id_imovel', help='Preenchimento obrigatório'),
    'endereco': fields.Nested(model_end),
    'tipo': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'gastos': fields.Nested(model_gastos),
    'idade': fields.Integer(required=True, description='tempo_propriedade', help='Preenchimento obrigatório')
})

model_cliente = app_.model('Cliente model', {
    'id': fields.Integer(required=True, description='id_proprietário', help='Preenchimento obrigatório'),
    'pessoa': fields.Nested(model_pessoa),
    'endereco': fields.Nested(model_end),
    'imovel': fields.List(fields.Nested(model_imovel))
})

model_transacoes = app_.model('Transacoes model', {
    'comprador': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'proprietario': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'imovel': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'pagamento': fields.Nested(model_pagamento)
})

########### IMPLEMENTAÇÃO DAS ROTAS ###########

@imoveis.route("/")
class MainClass(Resource):
    @app_.expect(model_imovel)
    def post(self):
        res = request.get_json()
        print(res)

@cliente.route("/")
class MainClass(Resource):
    @app_.expect(model_cliente)
    def post(self):
        res = request.get_json()

        posicao = len(res['imovel']) - 1
        
        nome = res['pessoa']['nome']
        cpf = res['pessoa']['cpf']
        data_nasc = res['pessoa']['data_nasc']
        rg = res['pessoa']['rg']
        profissao = res['pessoa']['profissao']
        estado_civil = res['pessoa']['estado_civil']

        rua_cliente = res['endereco']['rua']
        numero_cliente = res['endereco']['numero']
        andar_cliente = res['endereco']['andar']
        bloco_cliente = res['endereco']['bloco']
        bairro_cliente = res['endereco']['bairro']
        cep_cliente = res['endereco']['cep']
        cidade_cliente = res['endereco']['cidade']
        uf_cliente = res['endereco']['uf']

        rua_imovel = res['imovel'][posicao]['endereco']['rua']
        numero_imovel = res['imovel'][posicao]['endereco']['numero']
        andar_imovel = res['imovel'][posicao]['endereco']['andar']
        bloco_imovel = res['imovel'][posicao]['endereco']['bloco']
        bairro_imovel = res['imovel'][posicao]['endereco']['bairro']
        cep_imovel = res['imovel'][posicao]['endereco']['cep']
        cidade_imovel = res['imovel'][posicao]['endereco']['cidade']
        uf_imovel = res['imovel'][posicao]['endereco']['uf']

        energia = res['imovel'][posicao]['gastos']['energia']
        agua = res['imovel'][posicao]['gastos']['agua']
        condominio = res['imovel'][posicao]['gastos']['condominio']
        propaganda = res['imovel'][posicao]['gastos']['propaganda']

        tipo = res['imovel'][posicao]['tipo']
        idade = res['imovel'][posicao]['idade']

        pessoa = Pessoa(nome, cpf, data_nasc, rg, profissao, estado_civil)
        db.session.add(pessoa)        
        db.session.commit()

        endereco_cliente = Endereco(rua_cliente, numero_cliente, andar_cliente, bloco_cliente, bairro_cliente, cep_cliente, cidade_cliente, uf_cliente)
        db.session.add(endereco_cliente)        
        db.session.commit()

        endereco_imovel = Endereco(rua_imovel, numero_imovel, andar_imovel, bloco_imovel, bairro_imovel, cep_imovel, cidade_imovel, uf_imovel)
        db.session.add(endereco_imovel)        
        db.session.commit()

        gastos = Gastos(energia, agua, condominio, propaganda)
        db.session.add(gastos)        
        db.session.commit()

        imovel = Imovel(endereco_imovel.id_endereco, tipo, gastos.id_gastos, idade)
        db.session.add(imovel)        
        db.session.commit()

        cliente = Cliente(pessoa.id_pessoa, endereco_cliente.id_endereco, imovel.id_imovel)
        db.session.add(cliente)        
        db.session.commit()

        return jsonify(res)

    def get(self):
        allClientes = Endereco.query.all()
        output = []
        return jsonify(output)


@transacoes.route("/")
class MainClass(Resource):
    @app_.expect(model_transacoes)
    def post(self):
        res = request.get_json()

        print(res)

if __name__ == '__main__':
    app.run(debug = True)