#!/usr/bin/env python3

from flask import Blueprint

usuarios = Blueprint("",__name__, url_prefix='/usuarios')

@usuarios.route('/')
def index():
    return 'Indice do usuario'