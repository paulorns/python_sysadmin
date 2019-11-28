#!/usr/bin/env python3

import requests as r
import json

url_api = 'http://gen-net.herokuapp.com/api/users'

# realizando requisicoes com o modulo request
# res = r.get(url_api)
# print(res.json())

dados = {
    "name":"Pablo",
    "email":"pablo@pedreira.com.ar",
    "password":"senhasecreta123"
}

# res = r.post(url_api,json=dados)
# print(res.json())

# res = r.get('http://gen-net.herokuapp.com/api/users?{}={}'.format('name','Pedro'))
# print(res.json())

# res = r.put(url_api + '/274',json=dados)
# print(res.json())

# res = r.delete(url_api + '/274',json=dados)
# print(r.get(url_api).json())