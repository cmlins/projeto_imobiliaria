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

end = app_.namespace('Endereco', descrition='Endereco')

class Endereco(db.Model):   
    __tablename__ = 'endereco'
    Id_endereco = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
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

model_end = app_.model('Endereco model', {
    'rua': fields.String(required=True, description='rua', help='Preenchimento obrigatório'),
    'numero': fields.String(required=True, description='numero', help='Preenchimento obrigatório'),
    'andar': fields.String(required=True, description='andar', help='Preenchimento obrigatório'),
    'bloco': fields.String(required=True, description='bloco', help='Preenchimento obrigatório'),
    'bairro': fields.String(required=True, description='bairro', help='Preenchimento obrigatório'),
    'cep': fields.String(required=True, description='cep', help='Preenchimento obrigatório'),
    'cidade': fields.String(required=True, description='cidade', help='Preenchimento obrigatório'),
    'uf': fields.String(required=True, description='uf', help='Preenchimento obrigatório')
})

@app.route('/test', methods=['GET'])
def test(): 
    return {
        'test':'teste'
    }

@app.route('/endereco', methods=['GET'])
def get():
    allEnderecos = Endereco.query.all()
    output = []
    for endereco in allEnderecos:
        currEndereco = {}
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

@app.route('/endereco', methods=['POST'])
def post():
    res = request.get_json()
    endereco = Endereco(
                    rua = res['rua'],
                    numero = res['numero'],
                    andar = res['andar'],
                    bloco = res['bloco'],
                    bairro = res['bairro'],
                    cep = res['cep'],
                    cidade = res['cidade'],
                    uf = res['uf'],
                    )
    db.session.add(endereco)
    db.session.commit()
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug = True)