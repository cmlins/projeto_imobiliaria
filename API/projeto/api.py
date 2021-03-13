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

end = app_.namespace('Endereço', descrition='Endereco')

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
    'Id_endereco': fields.Integer(required=True, description='id', help='Preenchimento obrigatório'),
    'rua': fields.String(required=True, description='rua', help='Preenchimento obrigatório'),
    'numero': fields.String(required=True, description='numero', help='Preenchimento obrigatório'),
    'andar': fields.String(required=True, description='andar', help='Preenchimento obrigatório'),
    'bloco': fields.String(required=True, description='bloco', help='Preenchimento obrigatório'),
    'bairro': fields.String(required=True, description='bairro', help='Preenchimento obrigatório'),
    'cep': fields.String(required=True, description='cep', help='Preenchimento obrigatório'),
    'cidade': fields.String(required=True, description='cidade', help='Preenchimento obrigatório'),
    'uf': fields.String(required=True, description='uf', help='Preenchimento obrigatório')
})

@end.route("/<int:id>")
class MainClass(Resource):

    # https://github.com/noirbizarre/flask-restplus/blob/master/examples/todo.py
    # https://betterprogramming.pub/building-restful-apis-with-flask-and-sqlalchemy-part-1-b192c5846ddd
    # https://flask-restplus.readthedocs.io/en/stable/example.html
        
    # @app.route('/endereco/<id>/', methods=['PUT'])
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

    def delete(self, id):
        end = Endereco.query.get_or_404(id)
        try:
            db.session.delete(end)
            db.session.commit()
            return(f'linha {id} excluida')
        except:
            return "Dado não deletado"

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

@end.route("/")
class MainClass(Resource):
    def index():
        return {"test": "teste"}

    # @app.route('/endereco', methods=['GET'])
    def get(self):
        allEnderecos = Endereco.query.all()
        output = []
        for endereco in allEnderecos:
            currEndereco = {}
            currEndereco['Id_endereco'] = endereco.Id_endereco
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

    # @app.route('/endereco', methods=['POST'])
    @app_.expect(model_end)
    def post(self):
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