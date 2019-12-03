#!/usr/bin/env python3

import flask
import json

from usuarios.blueprint import usuarios_route # `A implementar
# from grupos.blueprint import grupos_routes # `A implementar
# from mensagens.blueprint import mensagens_routes # `A implementar

app = flask.Flask(__name__)
app.register_blueprint(usuarios_route)
# app.register_blueprint(grupos_routes)
# app.register_blueprint(mensagens_routes)

@app.route('/')
def index():
    return None

if __name__ == '__main__':
    app.run(debug=True)