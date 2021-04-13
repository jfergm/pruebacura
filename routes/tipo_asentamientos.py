from flask import Blueprint, request
from controllers.tipo_asentamientos_controller import *
tipo_asentamientos_bp = Blueprint('tipos_asentamiento', __name__)

@tipo_asentamientos_bp.route('/', methods=['GET', 'POST'])
def municipios():
  if(request.method == 'GET'):
    return obtener_tipo_asentamientos()
  elif(request.method == 'POST'):
    return crear_tipo_asentamiento(request.get_json())

@tipo_asentamientos_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def municipio(id):
  if(request.method == 'GET'):
    return obtener_tipo_asentamiento(id)
  elif(request.method == 'PATCH'):
    return actualizar_tipo_asentamiento(id, request.get_json())
  elif(request.method == 'DELETE'):
    return eliminar_tipo_asentamiento(id)
