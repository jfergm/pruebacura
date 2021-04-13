from app import db
from models.tipo_asentamiento import TipoAsentamiento
from flask import jsonify

def obtener_tipo_asentamientos():
  return jsonify([ta.serialize for ta in TipoAsentamiento.query.all()])

def obtener_tipo_asentamiento(id):
  return jsonify(TipoAsentamiento.query.get(id).serialize)

def crear_tipo_asentamiento(estado):
  nuevo_tipo_asentamiento = TipoAsentamiento(d_tipo_asenta=estado['d_tipo_asenta'])
  db.session.add(nuevo_tipo_asentamiento)
  db.session.commit()

  return jsonify(nuevo_tipo_asentamiento.serialize)

def actualizar_tipo_asentamiento(id, tipo_asentamiento_data):
  tipo_asentamiento = TipoAsentamiento.query.get(id)

  tipo_asentamiento.d_tipo_asenta = tipo_asentamiento_data['d_tipo_asenta'] if tipo_asentamiento_data['d_tipo_asenta'] else tipo_asentamiento.d_tipo_asenta

  db.session.commit()

  return jsonify(tipo_asentamiento.serialize)

def eliminar_tipo_asentamiento(id):
  tipo_asentamiento = TipoAsentamiento.query.get(id)
  db.session.delete(tipo_asentamiento)
  db.session.commit()

  return jsonify(tipo_asentamiento.serialize)