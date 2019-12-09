import flask
import jenkins

jenkins_routes = flask.Blueprint(name='jenkins', import_name=__name__,url_prefix='/jenkins')

@jenkins_routes.route('/')
def index():
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        # Criando a conexao com o Jenkins
        client = jenkins.Jenkins('http://localhost:8080',username='admin', password='admin')
        # Coletando os jobs que temos no jenkins
        jobs_list = client.get_jobs()
        jobs = []

        for job in jobs_list:
            jobs.append(client.get_job_info(job['fullname']))
    except Exception as e:
        print(e)
        jobs = []
    return flask.render_template('jenkins.jinja', jobs=jobs)

@jenkins_routes.route('/build/<string:job_name>')
def jenkins_build(job_name):
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        # Criando a conexao com o Jenkins
        client = jenkins.Jenkins('http://localhost:8080',username='admin', password='admin')
        client.build_job(job_name)
    except Exception as e:
        print(e)
    
    return flask.redirect(flask.url_for('jenkins.index'))

@jenkins_routes.route('/update/<string:job_name>')
def jenkins_update(job_name):
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        # Criando a conexao com o Jenkins
        client = jenkins.Jenkins('http://localhost:8080',username='admin', password='admin')
        job = {
            'name':job_name,
            'xml':client.get_job_config(job_name)
        }
    except Exception as e:
        print(e)
    # Apos o teste de conexcao, se der certo, ele redireciona para o
    # formulario de atualizacao e passa a variavel 'job'
    return flask.render_template('jenkins_update.jinja', job=job)

@jenkins_routes.route('/rebuild', methods=['POST'])
def jenkins_rebuild():
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    data = flask.request.form
    try:
        # Criando a conexao com o Jenkins
        client = jenkins.Jenkins('http://localhost:8080',username='admin', password='admin')
        client.reconfig_job(data['name'], data['xml'])
        # Se der certo, ele redireciona para o Index
        return flask.redirect(flask.url_for('jenkins.index'))
    except Exception as e:
        # Caso de erro, ele retorna para o formulario
        return flask.redirect(flask.url_for('jenkins.update', job_name=data['name']))
