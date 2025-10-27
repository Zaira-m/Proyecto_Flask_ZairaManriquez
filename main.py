from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con botones
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1: Promedio de notas y asistencia
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = round((nota1 + nota2 + nota3) / 3, 1)
            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

            resultado = f"Promedio: {promedio} - Estado: {estado}"
        except ValueError:
            resultado = "Por favor, ingresa valores numéricos válidos."

    return render_template('ejercicio1.html', resultado=resultado)

# Ejercicio 2: Nombre más largo
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        largo = len(nombre_mas_largo)

        resultado = f"El nombre más largo es '{nombre_mas_largo}' con {largo} caracteres."

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)