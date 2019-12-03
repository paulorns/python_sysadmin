from pymongo import MongoClient

# Criando a conexao com o Banco
mongo_con = MongoClient()

# Usar o Banco
db = mongo_con['flask-app']