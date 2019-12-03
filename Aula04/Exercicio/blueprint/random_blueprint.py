import flask
import random

# Variavel = flask.Blueprint('nome_da_blueprint',arquivo,'/caminho_do_arquivo')
random_blueprint = flask.Blueprint('random',__name__,url_prefix='/random')

@random_blueprint.route('/') # criando o decorador
def index():
    return str(random.randint(1,100))
    # Transformar o retorno em uma string, pois o codigo espera
    # receber uma string