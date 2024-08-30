from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)
data_file = 'data.xlsx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los datos del formulario
    data = {
        'Nombre': request.form['name'],
        'Número de identificación': request.form['id'],
        'Email': request.form['email'],
        'Nombre de la práctica': request.form['practice-name'],
        'Materia': request.form['subject'],
        'Profesor': request.form['professor'],
        'Aula': request.form['classroom'],
        'Tiempo de uso': request.form['tiempo-uso'],
        'Número de equipo': request.form['numero-equipo']
    }

    # Leer el archivo Excel
    df = pd.read_excel(data_file)

    # Añadir los datos nuevos
    df = df.append(data, ignore_index=True)

    # Guardar el archivo Excel
    df.to_excel(data_file, index=False)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
