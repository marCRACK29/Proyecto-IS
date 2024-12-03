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
    if request.method == 'POST':
        rut = request.form.get('rut')
        name = request.form.get('name')

        # Inserción del nuevo usuario en la base de datos, incluyendo la contraseña
        query = "INSERT INTO Patient (rut, name) VALUES (%s, %s);"
        database.cursor.execute(query, (rut, name))
        session['user'] = {"rut": rut, "name": name}

        return redirect(url_for('index'))

    return render_template('register.html')

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


@app.route('/api/createAppointment', methods=['PUT'])
def createAppointment():
	data = json.loads(request.data)

	agendaID = data["agendaID"]

	rutM = data["rutM"]
	rutP = session['user']['rut']

	database.createAppointment(agendaID, rutM, rutP)

	return jsonify(data)

# API para obtener agenda de un médico
@app.route('/api/medic/<rut>/agenda', methods=['GET'])
def getMedicAgenda(rut):
	agendas = database.getAgenda(rut)
	data = []

	for agenda in agendas:
		data.append({
			'ID': agenda.ID,
			'rutM': agenda.rutM,
			'day': agenda.start.strftime("%A %d"),
			'month': agenda.start.strftime("%B"),
			'year': agenda.start.strftime("%Y"),
			'time': agenda.start.strftime("%H:%M"),
		})

	return jsonify(data)

if __name__ == "__main__":
	app.run()
