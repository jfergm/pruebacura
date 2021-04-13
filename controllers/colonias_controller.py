from app import db
from models.colonia import Colonia
from flask import jsonify

def obtener_colonias():
  return jsonify([c.serialize for c in Colonia.query.all()])

def obtener_colonia(id):
  return jsonify(Colonia.query.get(id).serialize)

def crear_colonia(colonia):
  nueva_colonia = Colonia(d_asenta=colonia['d_asenta'], d_zona=colonia['d_zona'], d_codigo=colonia['d_codigo'], c_tipo_asenta=colonia['c_tipo_asenta'], c_mnpio=colonia['c_mnpio'])
  db.session.add(nueva_colonia)
  db.session.commit()

  return jsonify(nueva_colonia.serialize)

def actualizar_colonia(id, colonia_data):
  colonia = Colonia.query.get(id)

  colonia.d_asenta = colonia_data['d_asenta'] if 'd_asenta' in colonia_data.keys() else colonia.d_asenta
  colonia.d_zona = colonia_data['d_zona'] if 'd_zona' in colonia_data.keys() else colonia.d_zona
  colonia.d_codigo = colonia_data['d_codigo'] if 'd_codigo' in colonia_data.keys() else colonia.d_codigo
  colonia.c_tipo_asenta = colonia_data['c_tipo_asenta'] if 'c_tipo_asenta' in colonia_data.keys() else colonia.c_tipo_asenta
  colonia.c_mnpio = colonia_data['c_mnpio'] if 'c_mnpio' in colonia_data.keys() else colonia.c_mnpio

  db.session.commit()

  return jsonify(colonia.serialize)

def eliminar_colonia(id):
  colonia = Colonia.query.get(id)
  db.session.delete(colonia)
  db.session.commit()

  return jsonify(colonia.serialize)