#!/usr/bin/env python3

# import emoji
# print(emoji.emojize('Ola :thumbs_up:'))

# import flask
#
# app = flask.Flask(__name__)
#
# dados = {
#     'acesso':'OK'
# }

# Configurando rotas
# @app.route('/')
# def index():
#     return flask.jsonify(dados)

# configurando tipos de requisicao
# @app.route("/api?<any('id','nome'):string>=<int:id>", methods=['POST'])
# def index_get_id(id):
#     dados = {'nome':f'nome do id: {id}'}
#     return flask.jsonify(dados)
#
# @app.route('/teste/<string:nome>/', methods=['POST','GET'])
# def teste(id):
#   return f'Testes retornando {nome}'
#
# @app.route('/teste/<string:nome>/meusarquivos',  methods=['POST', 'GET'])
# def teste_teste():
#     return f'Testes retornando {nome} meus arquivos'
#
# app.run(host='0.0.0.0',debug=True,port=80)