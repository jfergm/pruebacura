from flask import Blueprint, request, jsonify
from controllers.estados_controller import *

estados_bp = Blueprint('estados', __name__)

@estados_bp.route('/', methods=['GET', 'POST'])
def estados():
  if(request.method == 'GET'):
    return obtener_estados()
  elif(request.method == 'POST'):
    return crear_estado(request.get_json())

@estados_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def estado(id):
  if(request.method == 'GET'):
    return obtener_estado(id)
  elif(request.method == 'PATCH'):
    return actualizar_estado(id, request.get_json())
  elif(request.method == 'DELETE'):
    return eliminar_estado(id)