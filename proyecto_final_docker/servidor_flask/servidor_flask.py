import os
import asyncio
import websockets
from flask import Flask, jsonify, redirect, render_template, request
from connectionbd import BaseDatos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/admin')  
def admin():
    return render_template('admin.html')  

@app.route('/reportes')  
def reportes():
    return render_template('reportes.html')  

@app.route('/facturacion')  
def facturacion():
    return render_template('factura.html')  

@app.route('/ticket')  
def ticket():
    return render_template('ticket.html')  

@app.route('/procesar_factura', methods=['POST'])
def procesar_factura():
    try:
        # Obtiene el número de tarjeta desde la solicitud JSON
        numero_tarjeta = request.json.get('numeroTarjeta')

        # Realiza el procesamiento necesario con el número de tarjeta
        bd = BaseDatos()  # Instanciamos la clase BaseDatos
        bd.connect()  # Conexión a la base de datos

        columnas = ['usuario_id', 'total_amount', 'descripcion', 'tarjeta']
        valores = ('1', '250.00', 'pago', numero_tarjeta)  # Los valores a insertar en las columnas correspondientes
        bd.insert('Facturacion', columnas, valores)


        return jsonify({"mensaje": "Factura procesada correctamente"})
    except Exception as e:
        print("Error al procesar la factura:", str(e))
        return jsonify({"error": f"Error al procesar la factura: {str(e)}"}), 500

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')  


async def main():

    await asyncio.gather(
        #app.run(port=5000, debug=True)
        app.run(host='0.0.0.0', port=5000, debug=True)

    )

if __name__ == "__main__":
    print("Servidor esperando conexiones...")
    app.run(debug=True)