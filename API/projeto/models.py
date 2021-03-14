model_end = app_.model('Endereco model', {
    'id_endereco': fields.Integer(required=True, description='id_endereco', help='Preenchimento obrigatório'),
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
    'data_nasc': fields.Date(required=True, description='data_nasc', help='Preenchimento obrigatório'),
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

model_imovel = app_.model('Imovel model', {
    'id_imovel': fields.Integer(required=True, description='id_imovel', help='Preenchimento obrigatório'),
    'id_endereco': fields.Integer(required=True, description='id_endereco', help='Preenchimento obrigatório'),
    'id_tipo': fields.Integer(required=True, description='id_tipo', help='Preenchimento obrigatório'),
})

model_proprietario = app_.model('Proprietario model', {
    'id_proprietário': fields.Integer(required=True, description='id_proprietário', help='Preenchimento obrigatório'),
    'id_pessoa': fields.Integer(required=True, description='id_pessoa', help='Preenchimento obrigatório'),
    'id_imovel': fields.Integer(required=True, description='id_imovel', help='Preenchimento obrigatório'),
    'id_gastos': fields.Integer(required=True, description='id_gastos', help='Preenchimento obrigatório'),
    'tempo_propriedade': fields.Integer(required=True, description='tempo_propriedade', help='Preenchimento obrigatório')
})

model_pagamento = app_.model('Pagamento model', {
    'id_pagamento': fields.Integer(required=True, description='id_pagamento', help='Preenchimento obrigatório'),
    'vista': fields.Boolean(required=True, description='vista', help='Preenchimento obrigatório'),
    'id_banco': fields.Integer(required=True, description='id_banco', help='Preenchimento obrigatório'),
    'entrada': fields.Integer(required=True, description='entrada', help='Preenchimento obrigatório'),
    'n_parcelas': fields.Integer(required=True, description='n_parcelas', help='Preenchimento obrigatório')
})

model_cliente = app_.model('Cliente model', {
    'id_cliente': fields.Integer(required=True, description='id_cliente', help='Preenchimento obrigatório'),
    'id_pessoa': fields.Integer(required=True, description='id_pessoa', help='Preenchimento obrigatório'),
    'id_endereco': fields.Integer(required=True, description='id_endereco', help='Preenchimento obrigatório'),
    'id_pagamento': fields.Integer(required=True, description='id_pagamento', help='Preenchimento obrigatório'),
    'id_imovel': fields.Integer(required=True, description='id_imovel', help='Preenchimento obrigatório')
})

model_proprietario = app_.model('Proprietario model', {
    'id_proprietário': fields.Integer(required=True, description='id_proprietário', help='Preenchimento obrigatório'),
    'pessoa': fields.Nested(model_pessoa),
    'imovel': fields.List(fields.Nested(model_imovel)),
    'tempo_propriedade': fields.Integer(required=True, description='tempo_propriedade', help='Preenchimento obrigatório'),
})

@end.route("/<int:id>")
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

