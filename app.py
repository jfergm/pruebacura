from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

from database import db

app = Flask(__name__)

def create_connection_string():
  type = os.environ.get('DATABASE_TYPE')
  host = os.environ.get('DATABASE_HOST')
  port = os.environ.get('DATABASE_PORT')
  name = os.environ.get('DATABASE_NAME')
  user = os.environ.get('DATABASE_USER')
  password = os.environ.get('DATABASE_PASSWORD')

  url = f'{type}://{user}:{password}@{host}:{port}/{name}'

  return url

app.config['SQLALCHEMY_DATABASE_URI'] = create_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():

  from models.estado import Estado
  from models.tipo_asentamiento import TipoAsentamiento
  from models.municipio import Municipio
  from models.colonia import Colonia

  db.create_all()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/estados')
def estados():
  return render_template('estados.html')

def register_blueprint():
  from routes.estados import estados_bp
  from routes.tipo_asentamientos import tipo_asentamientos_bp
  from routes.municipios import municipios_bp
  from routes.colonias import colonias_bp

  app.register_blueprint(estados_bp, url_prefix='/api/estados/')
  app.register_blueprint(tipo_asentamientos_bp, url_prefix='/api/tipo_asentamientos/')
  app.register_blueprint(municipios_bp, url_prefix='/api/municipios/')
  app.register_blueprint(colonias_bp, url_prefix='/api/colonias/')

if __name__ == '__main__':
    register_blueprint()
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)


