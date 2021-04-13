from flask import Flask
from routes.estados import estados_bp
from routes.municipios import municipios_bp
from routes.colonias import colonias_bp
from routes.tipo_asentamientos import tipo_asentamientos_bp

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello world'

app.register_blueprint(estados_bp, url_prefix='/api/estados/')
app.register_blueprint(municipios_bp, url_prefix='/api/municipios/')
app.register_blueprint(colonias_bp, url_prefix='/api/colonias/')
app.register_blueprint(tipo_asentamientos_bp, url_prefix='/api/tipo_asentamientos')

if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')