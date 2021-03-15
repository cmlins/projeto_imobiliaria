'''
Desenvolvedora: Cinthya Moreira Lins
cinthyalins@gmail.com
github: cmlins
'''

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app_ = Api(app=app, version='1.0', title='Imobiliaria', description='Sistema de venda de imóveis')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/Imobiliaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
app.secret_key = "alquimia"
db = SQLAlchemy(app)
CORS(app)

########### ÁREAS DO SWAGGER ###########

cliente = app_.namespace('Clientes', descrition='Cliente')
transacoes = app_.namespace('Transações', descrition='Transações')
imoveis = app_.namespace('Imoveis', descrition='Imoveis')
pessoas = app_.namespace('Pessoas', descrition='Dados pessoais dos clientes')
enderecos = app_.namespace('Endereços', descrition='Imoveis')

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
    'vista': fields.Integer(required=True, description='vista', help='Preenchimento obrigatório'),
    'id_banco': fields.Integer(required=True, description='id_banco', help='Preenchimento obrigatório'),
    'entrada': fields.Integer(required=True, description='entrada', help='Preenchimento obrigatório'),
    'n_parcelas': fields.Integer(required=True, description='n_parcelas', help='Preenchimento obrigatório')
})

model_cliente = app_.model('Cliente model', {
    'id': fields.Integer(required=True, description='id_proprietário', help='Preenchimento obrigatório'),
    'pessoa': fields.Nested(model_pessoa),
    'endereco': fields.Nested(model_end)
})

model_imovel = app_.model('Imovel model', {
    'id': fields.Integer(required=True, description='id_imovel', help='Preenchimento obrigatório'),
    'endereco': fields.Nested(model_end),
    'tipo': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'gastos': fields.Nested(model_gastos),
    'idade': fields.Integer(required=True, description='tempo_propriedade', help='Preenchimento obrigatório'),
    'proprietario': fields.Nested(model_cliente)
})

model_transacoes = app_.model('Transacoes model', {
    'id_comprador': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'id_proprietario': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'id_imovel': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
    'pagamento': fields.Nested(model_pagamento)
})

########### IMPLEMENTAÇÃO DAS ROTAS ###########

@pessoas.route("/")
class MainClass(Resource):
    def get(self):
        allPessoas = Pessoa.query.all()
        output = []
        for pessoa in allPessoas:
            currPessoa = {}
            currPessoa['id_pessoa'] = pessoa.id_pessoa
            currPessoa['nome'] = pessoa.nome
            currPessoa['cpf'] = pessoa.cpf
            currPessoa['data_nasc'] = pessoa.data_nasc
            currPessoa['rg'] = pessoa.rg
            currPessoa['profissao'] = pessoa.profissao
            currPessoa['estado_civil'] = pessoa.estado_civil
            output.append(currPessoa)
        return jsonify(output)

@pessoas.route("/<int:id>")
class MainClass(Resource):

    @app_.expect(model_pessoa)
    def put(self, id):
        res = request.get_json()

        pes = Pessoa.query.get(id)
        pes.cpf = res['cpf']
        pes.data_nasc = res['data_nasc']
        pes.estado_civil = res['estado_civil']
        pes.nome = res['nome']
        pes.profissao = res['profissao']
        pes.rg = res['rg']
        db.session.commit()

        return {
            'cpf': pes.cpf,
            'data_nasc': pes.numero,
            'estado_civil': pes.estado_civil,
            'nome': pes.nome,
            'profissao': pes.profissao,
            'rg': pes.rg,
        }

    def get(self, id):
        pes = Endereco.query.get(id)
        return {
            'rua': pes.rua,
            'numero': pes.numero,
            'andar': pes.andar,
            'bloco': pes.bloco,
            'bairro': pes.bairro,
            'cep': pes.cep,
            'cidade': pes.cidade,
            'uf': pes.uf
        }


########### ROTAS ENDEREÇO ###########

@enderecos.route("/<int:id>")
class MainClass(Resource):
    @app_.expect(model_end)
    def put(self, id):
        res = request.get_json()

        end = Endereco.query.get(id)
        end.rua = res['rua']
        end.numero = res['numero']
        end.andar = res['andar']
        end.bloco = res['bloco']
        end.bairro = res['bairro']
        end.cep = res['cep']
        end.cidade = res['cidade']
        end.uf = res['uf']
        db.session.commit()

        return {
            'rua': end.rua,
            'numero': end.numero,
            'andar': end.andar,
            'bloco': end.bloco,
            'bairro': end.bairro,
            'cep': end.cep,
            'cidade': end.cidade,
            'uf': end.uf
        }

    def get(self, id):
        end = Endereco.query.get(id)
        return {
            'rua': end.rua,
            'numero': end.numero,
            'andar': end.andar,
            'bloco': end.bloco,
            'bairro': end.bairro,
            'cep': end.cep,
            'cidade': end.cidade,
            'uf': end.uf
        }

@enderecos.route("/")
class MainClass(Resource):
    def get(self):
        allEnderecos = Endereco.query.all()
        output = []
        for endereco in allEnderecos:
            currEndereco = {}
            currEndereco['id_endereco'] = endereco.id_endereco
            currEndereco['rua'] = endereco.rua
            currEndereco['numero'] = endereco.numero
            currEndereco['andar'] = endereco.andar
            currEndereco['bloco'] = endereco.bloco
            currEndereco['bairro'] = endereco.bairro
            currEndereco['cep'] = endereco.cep
            currEndereco['cidade'] = endereco.cidade
            currEndereco['uf'] = endereco.uf
            output.append(currEndereco)
        return jsonify(output)

########### ROTAS IMOVEL ###########

@imoveis.route("/")
class MainClass(Resource):
    @app_.expect(model_imovel)
    def post(self):
        res = request.get_json()

        rua_imovel = res['endereco']['rua']
        numero_imovel = res['endereco']['numero']
        andar_imovel = res['endereco']['andar']
        bloco_imovel = res['endereco']['bloco']
        bairro_imovel = res['endereco']['bairro']
        cep_imovel = res['endereco']['cep']
        cidade_imovel = res['endereco']['cidade']
        uf_imovel = res['endereco']['uf']

        energia = res['gastos']['energia']
        agua = res['gastos']['agua']
        condominio = res['gastos']['condominio']
        propaganda = res['gastos']['propaganda']

        tipo = res['tipo']
        idade = res['idade']

        # proprietario
        nome = res['proprietario']['pessoa']['nome']
        cpf = res['proprietario']['pessoa']['cpf']
        data_nasc = res['proprietario']['pessoa']['data_nasc']
        rg = res['proprietario']['pessoa']['rg']
        profissao = res['proprietario']['pessoa']['profissao']
        estado_civil = res['proprietario']['pessoa']['estado_civil']

        rua_cliente = res['proprietario']['endereco']['rua']
        numero_cliente = res['proprietario']['endereco']['numero']
        andar_cliente = res['proprietario']['endereco']['andar']
        bloco_cliente = res['proprietario']['endereco']['bloco']
        bairro_cliente = res['proprietario']['endereco']['bairro']
        cep_cliente = res['proprietario']['endereco']['cep']
        cidade_cliente = res['proprietario']['endereco']['cidade']
        uf_cliente = res['proprietario']['endereco']['uf']        

        pessoa = Pessoa(nome, cpf, data_nasc, rg, profissao, estado_civil)
        db.session.add(pessoa)        
        db.session.commit()

        endereco_cliente = Endereco(rua_cliente, numero_cliente, andar_cliente, bloco_cliente, bairro_cliente, cep_cliente, cidade_cliente, uf_cliente)
        db.session.add(endereco_cliente)        
        db.session.commit()        

        cliente = Cliente(pessoa.id_pessoa, endereco_cliente.id_endereco)
        db.session.add(cliente)        
        db.session.commit()

        endereco_imovel = Endereco(rua_imovel, numero_imovel, andar_imovel, bloco_imovel, bairro_imovel, cep_imovel, cidade_imovel, uf_imovel)
        db.session.add(endereco_imovel)        
        db.session.commit()

        gastos = Gastos(energia, agua, condominio, propaganda)
        db.session.add(gastos)        
        db.session.commit()

        imovel = Imovel(endereco_imovel.id_endereco, tipo, gastos.id_gastos, idade, cliente.id_cliente)
        db.session.add(imovel)        
        db.session.commit()

        print(res)

    def get(self):
        allImoveis = Imovel.query.all()
        output = []
        for imovel in allImoveis:
            currImovel = {}
            currImovel['id_imovel'] = imovel.id_imovel
            currImovel['id_endereco'] = imovel.id_endereco
            currImovel['id_tipo'] = imovel.id_tipo
            currImovel['id_gastos'] = imovel.id_gastos
            currImovel['id_cliente'] = imovel.id_cliente
            currImovel['idade'] = imovel.idade
            output.append(currImovel)

        return jsonify(output)

@imoveis.route("/tipo")
class MainClass(Resource):
    def get(self):
        tipos = Tipo.query.all()
        output = []
        for tipo in tipos:
            currTipo = {}
            currTipo['id_tipo'] = tipo.id_tipo
            currTipo['tipo'] = tipo.tipo
            output.append(currTipo)
        return jsonify(output)

@imoveis.route("/gastos")
class MainClass(Resource):
    def get(self):
        gastos = Gastos.query.all()
        output = []
        for gasto in gastos:
            currGasto = {}
            currGasto['id_gastos'] = gasto.id_gastos
            currGasto['energia'] = gasto.energia
            currGasto['agua'] = gasto.agua
            currGasto['condominio'] = gasto.condominio
            currGasto['propaganda'] = gasto.propaganda
            output.append(currGasto)
        return jsonify(output)

@imoveis.route("/<int:id>")
class MainClass(Resource):
    def delete(self, id):
        imo = Imovel.query.get_or_404(id)
        end = Endereco.query.get_or_404(imo.id_endereco)
        gas = Gastos.query.get_or_404(imo.id_gastos)
        try:
            db.session.delete(gas)
            db.session.delete(end)
            db.session.delete(imo)
            db.session.commit()
            return(f'Imovel {id} excluido')
        except:
            return "Imovel não deletado"

########### ROTAS CLIENTE ###########

@cliente.route("/")
class MainClass(Resource):
    @app_.expect(model_cliente)
    def post(self):
        res = request.get_json()
       
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

        pessoa = Pessoa(nome, cpf, data_nasc, rg, profissao, estado_civil)
        db.session.add(pessoa)        
        db.session.commit()

        endereco_cliente = Endereco(rua_cliente, numero_cliente, andar_cliente, bloco_cliente, bairro_cliente, cep_cliente, cidade_cliente, uf_cliente)
        db.session.add(endereco_cliente)        
        db.session.commit()        

        cliente = Cliente(pessoa.id_pessoa, endereco_cliente.id_endereco)
        db.session.add(cliente)        
        db.session.commit()

        return jsonify(res)

    def get(self):
        allClientes = Cliente.query.all()
        output = []
        for cliente in allClientes:
            currCliente = {}
            currCliente['id_cliente'] = cliente.id_cliente
            currCliente['id_pessoa'] = cliente.id_pessoa
            currCliente['id_endereco'] = cliente.id_endereco
            output.append(currCliente)

        return jsonify(output)        

@cliente.route("/<int:id>")
class MainClass(Resource):
    
    def delete(self, id):
        cli = Cliente.query.get_or_404(id)
        pes = Pessoa.query.get_or_404(cli.id_pessoa)
        end = Endereco.query.get_or_404(cli.id_endereco)
        try:
            db.session.delete(cli)
            db.session.delete(pes)
            db.session.delete(end)
            db.session.commit()
            return(f'Cliente {id} excluido')
        except:
            return "Cliente não deletado"

    def get(self, id):
        cli = Cliente.query.get(id)
        return {
            'id_cliente': cliente.id_cliente,
            'id_pessoa': cliente.id_pessoa,
            'id_endereco': cliente.id_endereco,
        }

########### ROTAS TRANSAÇÕES ###########

@transacoes.route("/")
class MainClass(Resource):
    @app_.expect(model_transacoes)
    def post(self):
        res = request.get_json()
        print(res)
        comprador = res['id_comprador']
        proprietario = res['id_proprietario']
        imovel = res['id_imovel']

        a_vista = res['pagamento']['vista']
        id_banco = res['pagamento']['id_banco']
        entrada = res['pagamento']['entrada']
        n_parcelas = res['pagamento']['n_parcelas']

        pagamento = Pagamento(a_vista, id_banco, entrada, n_parcelas)
        db.session.add(pagamento)
        db.session.commit()

        transacao = Transacao(imovel, comprador, proprietario, pagamento.id_pagamento)
        db.session.add(transacao)
        db.session.commit()

        imovel = Imovel.query.get_or_404(imovel)
        imovel.id_cliente = transacao.id_comprador
        db.session.commit()


        print(res)

    def get(self):
        allTransacoes = Transacao.query.all()
        output = []
        for transacao in allTransacoes:
            currTransacao = {}
            currTransacao['id_comprador'] = transacao.id_comprador
            currTransacao['id_proprietario'] = transacao.id_proprietario
            currTransacao['id_imovel'] = transacao.id_imovel
            
            output.append(currTransacao)

        return jsonify(output)

if __name__ == '__main__':
    app.run(debug = True)