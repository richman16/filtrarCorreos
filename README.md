# Seperar datos de una fila en 2 filas

_Este programa desarollado en python y Flask, lee un archivo CSV y descompone ciertas columas repetidas de una fila en dos filas en un archivo de salida CSV_

## Ejemplo de filtrado de emails

_En este caso estamos filtrando correos electronicos de un archivo CSV, el cual es una base de datos de alumnos y padres de familias. En este caso el archivo de entrada tiene 4 columnas con los datos de los padres y madres, con su nombre y correo. Se quiere obtner una lista solo de los nombres y correos de los padres._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
python3
virtualenv
pip
pandas
Flask

```

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Clonar repositorio_

```bash
git clone https://github.com/richman16/filtrarCorreos
cd filtrarCorreos
```

_Ejecutar ambiente virtual_

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```
_3 Ejecuta Flask_

```bash
python3 app.py
```

_4 Abrir link_

```
http://127.0.0.1:5000/
```

## Ejecutando ⚙️

_Se proporciona un archivo de muestra CSV_
```
alumnosDatos.csv
```

```
1. Selecciona un archivo CSV que cumpla con los requisitos especificados.
2. Haz clic en el botón "Procesar" para generar el nuevo archivo CSV con la información filtrada.
3. Descarga el archivo resultante
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_
