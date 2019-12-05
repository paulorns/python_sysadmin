import flask
# import docker

from blueprints.docker_blueprint import docker_routes

app = flask.Flask(__name__)

app.register_blueprint(docker_routes)

@app.route('/')
def index():
    return flask.render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)