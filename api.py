import sys
import os

# Establecer la variable de entorno antes de importar TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')))

from main import ChatBot
from flask import Flask, jsonify, request

app = Flask(__name__)

modelo = None

@app.route('/')
def inicio():
    return 'Esta funcionando...'

@app.route('/pregunta', methods=['POST'])
def darPregunta():
    pregunta = request.get_json()
    pregunta = pregunta.get('message')
    respuesta = modelo.procesar(pregunta)
    print("Respuesta: ", respuesta)
    return jsonify({ 
        'respuesta': respuesta 
    })

@app.route('/pregunta', methods=['GET'])
def darPreguntaGet():
    pregunta = request.args.get('message')
    respuesta = modelo.procesar(pregunta)
    print("Respuesta: ", respuesta)
    return jsonify({ 
        'respuesta': respuesta 
    })

if __name__ == '__main__':
    modelo = ChatBot()
    modelo.cargar()
    port = int(os.getenv("PORT", 5000))  # Use el puerto dinámico proporcionado por Render
    app.run(host='0.0.0.0', port=port)
