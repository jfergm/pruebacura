from flask import Blueprint, request

municipios_bp = Blueprint('municipios', __name__)

@municipios_bp.route('/', methods=['GET', 'POST'])
def municipios():
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'POST'):
    return ''

@municipios_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def municipio(id):
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'PATCH'):
    return ''
  elif(request.method == 'DELETE'):
    return ''
