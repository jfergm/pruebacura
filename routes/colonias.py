from flask import Blueprint, request

colonias_bp = Blueprint('colonias', __name__)

@colonias_bp.route('/', methods=['GET', 'POST'])
def colonias():
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'POST'):
    return ''

@colonias_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def colonia(id):
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'PATCH'):
    return ''
  elif(request.method == 'DELETE'):
    return ''