import sys
import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session

from back import *

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Cargar base de datos
access = json.loads(open(sys.path[0] + "/back/db/db-data.json").read())
database = DataBase(access)


# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear() # Limpiar la sesión
    if request.method == 'POST':
        rut = request.form.get('rut')
        name = request.form.get('name')

        # Verificar paciente en la base de datos
        query = "SELECT * FROM Patient WHERE rut = %s;"
        database.cursor.execute(query, (rut,))
        patient = database.cursor.fetchone()

        if patient:
            # Guardar información del usuario en la sesión
            session['user'] = {"rut": rut, "name": patient[1]}
            return redirect(url_for('index'))
        else:
            return redirect(url_for('register', rut=rut))

    # Mostrar formulario de login
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    rut = request.args.get('rut')  # Recuperar el RUT desde la redirección

    if request.method == 'POST':
        rut = request.form.get('rut')
        name = request.form.get('name')

        # Insertar el nuevo usuario en la base de datos
        query = "INSERT INTO Patient (rut, name) VALUES (%s, %s);"
        database.cursor.execute(query, (rut, name))
        session['user'] = {"rut": rut, "name": name}

        return redirect(url_for('index'))

    return render_template('register.html', rut=rut)

@app.before_request
def clear_session_on_index():
    # Limpiar la sesión solo si el usuario intenta acceder al índice sin estar logueado
    if request.endpoint == 'index' and 'user' not in session:
        session.clear()

# Ruta del catálogo (restringida)
@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('catalog.html')


# API para obtener médicos
@app.route('/api/medics', methods=['GET'])
def getMedics():
    medics = database.getMedics()
    medicsData = []

    for medic in medics:
        medicsData.append({
            'name': medic.name,
            'speciality': medic.area,
            'rut': medic.rut
        })

    return jsonify(medicsData)


# API para obtener agenda de un médico
@app.route('/api/medic/<rut>/agenda', methods=['GET'])
def getMedicAgenda(rut):
    try:
        query = "SELECT ID, rutM, start, free FROM Agenda WHERE rutM = %s;"
        database.cursor.execute(query, (rut,))
        data = database.cursor.fetchall()
        agenda_list = [
            {"id": row[0], "rutM": row[1], "start": row[2], "free": row[3]}
            for row in data
        ]
        return jsonify(agenda_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
