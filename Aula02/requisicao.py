#!usr/bin/env python3

# DECORATOR --
# def vermelho(retorno_funcao):
#    def modificaCor(retorno_funcao):
#        return f'\033[91m{retorno_funcao}\033[0m'
#    return modificaCor
#
# @vermelho # Decorator - Recebe o retorno da funcao abaixo e executa
# def texto(texto):
#    return texto
#
#print(texto('Uma palavra'))


# import requests as r
#
# data = {
#     "name":"Abner"
# }
#
# res = r.get('http://gen-net.herokuapp.com/api/users', params=data)
# print(res.json())

import requests

res = requests.post('http://127.0.0.1/api?id=12')
print(res)
# res = res.json()
# print(res['nome'])