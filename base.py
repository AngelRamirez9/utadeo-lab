from flask import Flask, request, jsonify
import xlsxwriter

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    # Crear o abrir un archivo Excel
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet()

    # Escribir los datos en el archivo
    worksheet.write('A1', 'Nombre')
    worksheet.write('B1', 'Número de identificación')
    worksheet.write('C1', 'Email')
    worksheet.write('D1', 'Tiempo de uso')
    worksheet.write('E1', 'Número de equipo')

    worksheet.write('A2', data.get('name'))
    worksheet.write('B2', data.get('id'))
    worksheet.write('C2', data.get('email'))
    worksheet.write('D2', data.get('tiempo-uso'))
    worksheet.write('E2', data.get('numero-equipo'))

    workbook.close()

    return jsonify({"message": "Datos guardados con éxito"}), 200

if __name__ == '__main__':
    app.run(debug=True)
