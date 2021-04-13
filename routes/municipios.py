from flask import Blueprint, request
from controllers.municipios_controller import *
municipios_bp = Blueprint('municipios', __name__)

@municipios_bp.route('/', methods=['GET', 'POST'])
def municipios():
  if(request.method == 'GET'):
    return obtener_municipios(request.args)
  elif(request.method == 'POST'):
    return crear_municipio(request.get_json())

@municipios_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def municipio(id):
  if(request.method == 'GET'):
    return obtener_municipio(id)
  elif(request.method == 'PATCH'):
    return actualizar_municipio(id, request.get_json())
  elif(request.method == 'DELETE'):
    return eliminar_municipio(id)
