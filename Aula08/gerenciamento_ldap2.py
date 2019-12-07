#!/usr/bin/env python3

import ldap3
from hashlib import md5
from binascii import b2a_base64

# Criando o usuario e senha de administrador
username = 'admin'
password = 'admin'

# Identificando o meu servidor
server = ldap3.Server('ldap://localhost:389')

# Criando a conexao
client = ldap3.Connection(server, f'cn={username},dc=exemple,dc=org',password)

client.bind()
# print(client)

#Inserindo um usu'ario na rede
md5json = md5('senhaSegura'.encode('utf-8')).digest()

user = {
    'cn':'Cleiton',
    'sn':'rasta',
    'mail':'aosom.dequem@cleitonrasta.com.br',
    'uidNumber':'1000',
    'gidNumber':'1000',
    'uid':'cleiton.rasta',
    'homeDirectory':'/home/joao',
    'userPassword':'{MD5}' + b2a_base64(md5json).decode('utf-8') # Inserindo a criptografia
}

objectClass = ['top','person','organizationalPerson','inetOrgPerson','posixAccount']

cn = 'uid='+user['mail']+',dc=example,dc=org'

print(client.add(cn,objectClass,user))