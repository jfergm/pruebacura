from app import db
from models.municipio import Municipio
from flask import jsonify

def obtener_municipios():
  return jsonify([m.serialize for m in Municipio.query.all()])

def obtener_municipio(id):
  return jsonify(Municipio.query.get(id).serialize)

def crear_municipio(municipio):
  nuevo_municipio = Municipio(d_mnpio=municipio['d_mnpio'], c_estado=municipio['c_estado'])
  db.session.add(nuevo_municipio)
  db.session.commit()

  return jsonify(nuevo_municipio.serialize)

def actualizar_municipio(id, municipio_data):
  municipio = Municipio.query.get(id)

  municipio.d_mnpio = municipio_data['d_mnpio'] if 'd_mnpio' in municipio_data.keys() else municipio.d_mnpio
  municipio.c_estado = municipio_data['c_estado'] if 'c_estado' in municipio_data.keys() else municipio.c_estado

  db.session.commit()

  return jsonify(municipio.serialize)

def eliminar_municipio(id):
  municipio = Municipio.query.get(id)
  db.session.delete(municipio)
  db.session.commit()

  return jsonify(municipio.serialize)