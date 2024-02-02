from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    if 'archivo' not in request.files:
        return render_template('index.html', mensaje='No se ha seleccionado ningún archivo.')

    archivo = request.files['archivo']

    if archivo.filename == '':
        return render_template('index.html', mensaje='No se ha seleccionado ningún archivo.')

    # Leer el archivo CSV o Excel
    try:
        df = pd.read_csv(archivo)  # Cambia a pd.read_excel si es necesario
    except pd.errors.EmptyDataError:
        return render_template('index.html', mensaje='El archivo está vacío o no es válido.')

    # Crear un DataFrame con las columnas deseadas
    df_padre = pd.DataFrame({
        'PersonaNombre': df['PadreNombre'],
        'PersonaApellidoP': df['PadreApellidoP'],
        'PersonaApellidoM': df['PadreApellidoM'],
        'PersonaCorreo': df['PadreCorreo']
    })
    # Concatenar los DataFrames de Padre y Madre
    df_output = pd.concat([df_padre], ignore_index=True)


    df_madre = pd.DataFrame({
        'PersonaNombre': df['MadreNombre'],
        'PersonaApellidoP': df['MadreApellidoP'],
        'PersonaApellidoM': df['MadreApellidoM'],
        'PersonaCorreo': df['MadreCorreo']
    })
    # Concatenar los DataFrames de Padre y Madre
    df_output = pd.concat([df_madre], ignore_index=True)

    # Crear el archivo CSV de salida
    output = BytesIO()
    df_output.to_csv(output, index=False)

    output.seek(0)

    return send_file(output, as_attachment=True, download_name='datos_personas_filtrados.csv')

if __name__ == '__main__':
    app.run(debug=True)
