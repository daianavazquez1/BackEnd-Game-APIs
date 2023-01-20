from flask import Flask, jsonify, request
from sqlinterface import Conexion 
import os

app = Flask(__name__)

def comprobacion(x,y):
    if x==y:
        return True
    else:
        return False

@app.route("/data", methods=["GET"])
def message():
    
    pj = request.args.get('Personajes')
    
    # Acá van los nombres de la base de datos y la tabla
    conexion = Conexion('tabla_api_juego', 'Personajes')

    data = conexion.consulta('select * from {} where {}=="{}"'.format(conexion.tabla, 'name', pj))
    nueva_data = [x[0] for x in data]
    salida = {'personaje': (data[0])}
    return salida

if __name__=='__main__':

    try:
        app.run(host='127.0.0.1',port=8008)

    except Exception as e:
        print(e)
        print("Setear variables de entorno ip y puerto")