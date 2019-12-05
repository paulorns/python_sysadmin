#!/usr/bin/env python3
import docker

# client = docker.Docker("tcp://127.0.0.1:2376") # Conexao remota
client = docker.from_env() # Conexao local
# client.containers.run('ubuntu:latest', 'echo hello world')
# client.containers.run('python','python --help') # Subindo o servico do Python
print(client.containers.list(all=True)) # Listando os containers que possui na m'aquina
# container = client.containers.get('jolly_torvalds')
# print(container.short_id) # Pegando o ID do container
# print(container.name) # Pegando o nome do container
# print(container.image.tags) # Pegando a imagem do container
# print(container.status) # Mostrando o status do container
# print(container.image.tags[0]) # Pegando a imagem do container, mostrando o resultado da lista

# container2 = client.containers.get('pensive_liskov')
# print(container2.short_id)
# print(container2.name)
# print(container2.image.tags)

# container3 = client.containers.get('jolly_torvalds')
# print(container3.short_id)
# print(container.name)
# print(container3.image.tags)

teste = client.containers.get('6634228dd0')
print(teste.name)
print(teste.image.tags)
print(teste.status)