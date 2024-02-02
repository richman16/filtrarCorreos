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
    df_output = pd.DataFrame()
    

    # Iterar sobre las filas del DataFrame original
    for index, row in df.iterrows():
        df_padre = pd.DataFrame()
        df_madre = pd.DataFrame()

        if pd.notna(row['PadreCorreo']):
            # Crear una fila para el Padre
            df_padre = pd.DataFrame({
                'PersonaNombre': row['PadreNombre'],
                'PersonaApellidoP': row['PadreApellidoP'],
                'PersonaApellidoM': row['PadreApellidoM'],
                'PersonaCorreo': row['PadreCorreo']
            }, index=[0])

        if pd.notna(row['MadreCorreo']):
            # Crear una fila para la Madre
            df_madre = pd.DataFrame({
                'PersonaNombre': row['MadreNombre'],
                'PersonaApellidoP': row['MadreApellidoP'],
                'PersonaApellidoM': row['MadreApellidoM'],
                'PersonaCorreo': row['MadreCorreo']
            }, index=[0])

        # Concatenar las filas en el DataFrame de salida
        """ if df_madre.empty:
            df_output = pd.concat([df_output, df_padre], ignore_index=True)
        elif df_padre.empty:
            df_output = pd.concat([df_output, df_madre], ignore_index=True)
        else:
            df_output = pd.concat([df_output, df_padre, df_madre], ignore_index=True) """
        
        df_output = pd.concat([df_output, df_padre, df_madre], ignore_index=True)

    # Filtrar filas vacías en el Data Frame de salida
    df_output = df_output.dropna(subset=['PersonaCorreo'])
    # Crear el archivo CSV de salida
    output = BytesIO()
    df_output.to_csv(output, index=False)

    output.seek(0)

    return send_file(output, as_attachment=True, download_name='datos_personas_filtrados.csv')

if __name__ == '__main__':
    app.run(debug=True)
