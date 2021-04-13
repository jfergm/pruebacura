from app import db

class Estado(db.Model):
  c_estado = db.Column(db.Integer, primary_key=True)
  d_estado = db.Column(db.String)

  @property
  def serialize(self):
    return {
      'c_estado': self.c_estado,
      'd_estado': self.d_estado
    }
