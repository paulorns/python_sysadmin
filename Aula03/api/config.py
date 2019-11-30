from pymongo import MongoClient

# Criando a conexao com o Banco
mongo_con = MongoClient()

# Usar o Banco
mongo_db = mongo_con['flask-app']