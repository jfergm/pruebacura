from flask import Blueprint, request

tipo_asentamientos_bp = Blueprint('tipos_asentamiento', __name__)

@tipo_asentamientos_bp.route('/', methods=['GET', 'POST'])
def municipios():
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'POST'):
    return ''

@tipo_asentamientos_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def municipio(id):
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'PATCH'):
    return ''
  elif(request.method == 'DELETE'):
    return ''
