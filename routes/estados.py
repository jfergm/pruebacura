from flask import Blueprint, request, jsonify

estados_bp = Blueprint('estados', __name__)

@estados_bp.route('/', methods=['GET', 'POST'])
def estados():
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'POST'):
    return ''

@estados_bp.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def colonia():
  if(request.method == 'GET'):
    return ''
  elif(request.method == 'PATCH'):
    return ''
  elif(request.method == 'DELETE'):
    return ''