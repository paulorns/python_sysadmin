from flask import Blueprint, request, Response
from config import db
from bson.json_util import dumps

usuarios_route = Blueprint('usuarios_route',__name__, url_prefix='/usuarios')

@usuarios_route.route('/', methods=["POST"])
def insert_user():
    try:
        user = request.get_json() # vai trazer um arquivo json
        db.user.insert_one(
            {
                'name':user['name'],
                'email':user['email'],
                'messages':[]
            }
        )
        response = {'message':f'Usuario {user["name"]}, criado com sucesso'}
        return Response(dumps(response),status=201)
    except Exception as e:
        erro = {'error':e}
        return Response(dumps(erro),status=500)

@usuarios_route.route('/', methods=['GET'])
def get_user():
    try:
        user = db.user.find()
        return Response(dumps(user), status=200)
    except Exception as e:
        erro = {'error':e}
        return Response(dumps(erro), status=500)

@usuarios_route.route('/', methods=['PATCH'])
def update_user():
    try:
        user = request.get_json()
        updated = db.user.update_one(
            {
                'email': user['email'],
                '$set': user
            }
        )
        if update.modified_count:
            response = {'message':f'Usuario {user["name"]}, atualizado com sucesso'}
            return Response(dumps(resopnse), status=200)
        if updated.matched_count:
            response = {'message':f'Usuario {user["name"]}, encontrado, porem nao modificado'}
            return Response(dumps(response), status=304)
        else:
            response = {'message':f'Usuario {user["name"]}, nao encontrado'}
            return Response(dumps(response), status=503)
    except Exception as e:
        erro = {'error': e}
        return Response(dumps(erro), status=500)

@usuarios_route.route('/', methods=['DELETE'])
def delete_user():
    try:
        user = request.get_json()
        updated = db.user.delete_one(
            {
                'email':user['email']
            }
        )
        if updated.deleted_count:
            response = {'message':f'Usuario {user["name"]}, deletado comsucesso'}
            return Response(dumps(resopnse), status=200)
        else:
            response = {'message':f'Usuario {user["name"]}, nao encontrado'}
            return Response(dumps(response), status=503)
    except Exception as e:
        erro = {'error': e}
        return Response(dumps(erro), status=500)