from flask import Flask
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
  print(url)
  return url

app.config['SQLALCHEMY_DATABASE_URI'] = create_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():

  from models.estado import Estado

  db.create_all()

@app.route('/')
def index():
  return 'Hello world'


def register_blueprint():
  from routes.estados import estados_bp

  app.register_blueprint(estados_bp, url_prefix='/api/estados/')

if __name__ == '__main__':
  register_blueprint()
  app.run(debug = True, host = '0.0.0.0')


