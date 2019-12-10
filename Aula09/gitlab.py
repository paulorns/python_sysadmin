import requests

token = 'aKcaFuAVEJre7L9UkxAG'

# Consultar projetos
# projetos = requests.get(f'http://localhost:81/api/v4/projects?private_token={token}')
# print(projetos.json())

# projeto = {
#     'name': 'batata-frita'
# }

# Adicionar projetos
# projetos = requests.post(f'http://localhost:81/api/v4/projects?private_token={token}',projeto)
# print(projetos.json())

# Consultar usuarios

# projetos = requests.get(f'http://localhost:81/api/v4/users?private_token={token}')
# print(projetos.json())

# Adicionar usuarios
usuario = {
    'email':'pedro.cardoso@gmail.com',
    'username':'pedro.cardoso',
    'name':'Pedro Cardoso',
    'password':'4linux'
}


projetos = requests.post(f'http://localhost:81/api/v4/users?private_token={token}',usuario)
print(projetos.json())

# Adicionar membros ao projeto
project_id = 1
pessoa = {
    'user_id':12,
    'access_level':40
}

projetos = requests.get(f'http://localhost:81/api/v4/projects/{project_id}?private_token={token}',pessoa)
print(projetos.json())