from app import db
from models.estado import Estado
from flask import jsonify

def obtener_estados():
  return jsonify([e.serialize for e in Estado.query.all()])

def obtener_estado(id):
  return jsonify(Estado.query.get(id).serialize)

def crear_estado(estado):
  nuevo_estado = Estado(d_estado=estado['d_estado'])
  db.session.add(nuevo_estado)
  db.session.commit()

  return jsonify(nuevo_estado.serialize)

def actualizar_estado(id, estado_data):
  estado = Estado.query.get(id)

  estado.d_estado = estado_data['d_estado'] if estado_data['d_estado'] else estado.d_estado

  db.session.commit()

  return jsonify(estado.serialize)

def eliminar_estado(id):
  estado = Estado.query.get(id)
  db.session.delete(estado)
  db.session.commit()

  return jsonify(estado.serialize)