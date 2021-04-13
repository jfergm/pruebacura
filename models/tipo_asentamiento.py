from app import db

class TipoAsentamiento(db.Model):
  c_tipo_asenta = db.Column(db.Integer, primary_key=True)
  d_tipo_asenta = db.Column(db.String)

  @property
  def serialize(self):
    return {
      'c_tipo_asenta': self.c_tipo_asenta,
      'd_tipo_asenta': self.d_tipo_asenta
    }