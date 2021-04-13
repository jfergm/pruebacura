from flask import Blueprint, request
from controllers.colonias_controller import *

colonias_bp = Blueprint('colonias', __name__)

@colonias_bp.route('/', methods=['GET', 'POST'])
def colonias():
  if(request.method == 'GET'):
    return obtener_colonias(request.args)
  elif(request.method == 'POST'):
    return crear_colonia(request.get_json())

@colonias_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def colonia(id):
  if(request.method == 'GET'):
    return obtener_colonia(id)
  elif(request.method == 'PATCH'):
    return actualizar_colonia(id, request.get_json())
  elif(request.method == 'DELETE'):
    return eliminar_colonia(id)