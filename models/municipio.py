from app import db

class Municipio(db.Model):
  c_mnpio = db.Column(db.Integer, primary_key=True)
  d_mnpio = db.Column(db.String)
  c_estado = db.Column(db.Integer, db.ForeignKey('estado.c_estado'))


  @property
  def serialize(self):
    return {
      'c_mnpio': self.c_mnpio,
      'd_mnpio': self.d_mnpio,
      'c_estado': self.c_estado
    }
