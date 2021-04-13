from app import db
from enum import Enum

class ZonaEnum(Enum):
  RURAL = 'Rural'
  URBANO = 'Urbano'

class Colonia(db.Model):
  id_asenta_cpcons = db.Column(db.Integer, primary_key=True)
  d_asenta = db.Column(db.String)
  d_zona = db.Column(db.String, db.Enum(ZonaEnum))
  d_codigo = db.Column(db.String)
  c_tipo_asenta = db.Column(db.Integer, db.ForeignKey('tipo_asentamiento.c_tipo_asenta'))
  c_mnpio = db.Column(db.Integer, db.ForeignKey('municipio.c_mnpio'))

  @property
  def serialize(self):
    return {
      'id_asenta_cpcons': self.id_asenta_cpcons,
      'd_asenta': self.d_asenta,
      'd_zona': self.d_zona,
      'd_codigo': self.d_codigo,
      'c_tipo_asenta': self.c_tipo_asenta,
      'c_mnpio': self.c_mnpio
    }

