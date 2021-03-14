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