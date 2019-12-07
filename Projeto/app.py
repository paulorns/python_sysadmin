import flask
# import docker

# Importando as rotas das blueprints
from blueprints.docker_blueprint import docker_routes
from blueprints.jenkins_blueprint import jenkins_routes
from blueprints.ldap_blueprint import ldap_routes

# Controle de aplicacao
app = flask.Flask(__name__)

# Registro de rotas
app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)
app.register_blueprint(ldap_routes)

@app.route('/')
def index():
    return flask.render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)